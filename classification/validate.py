"""Validate literature metadata, not algorithm correctness. Requires jsonschema."""
import argparse
import copy
import csv
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]


def read_json(name):
    return json.loads((BASE / name).read_text())


def read_csv(name):
    with (BASE / name).open(newline='') as handle:
        return list(csv.DictReader(handle))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-sources', action='store_true', help='Verify local PDF paths and recorded SHA-256 hashes')
    args = parser.parse_args()
    schema = read_json('record.schema.json')
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    dimensions = read_csv('dimensions.csv')
    vocabulary = {row['dimension']: row['allowed_values'].split('|') for row in dimensions}
    require(len(vocabulary) == len(dimensions), 'Duplicate dimension IDs')
    claim_schema = schema['properties']['claims']['items']
    require(set(claim_schema['properties']['dimension']['enum']) == set(vocabulary), 'Schema/dictionary dimensions differ')
    for rule in claim_schema['allOf']:
        key = rule.get('if', {}).get('properties', {}).get('dimension', {}).get('const')
        if key:
            require(rule['then']['properties']['values']['items']['enum'] == vocabulary[key], f'Vocabulary mismatch: {key}')
    sources = read_json('sources.json')
    source_ids = {source['id'] for source in sources}
    require(len(source_ids) == len(sources), 'Duplicate source IDs')
    tests = read_csv('test-families.csv')
    test_ids = {test['test_id'] for test in tests}
    require(len(test_ids) == len(tests), 'Duplicate test IDs')
    require(set(schema['properties']['test_ids']['items']['enum']) == test_ids, 'Schema/test catalogue differs')
    examples = read_json('examples.json')
    require(len({record['record_id'] for record in examples}) == len(examples), 'Duplicate example IDs')
    template = read_json('record-template.json')
    require({claim['dimension'] for claim in template['claims']} == set(vocabulary), 'Template is missing dimensions')
    for record in [template, *examples]:
        validator.validate(record)
        rid = record['record_id']
        record_sources = set(record['source_ids'])
        require(record_sources <= source_ids, f'{rid}: unresolved record sources')
        require(len({c['dimension'] for c in record['claims']}) == len(record['claims']), f'{rid}: duplicate facet; consolidate claims or split configurations')
        for claim in record['claims']:
            require(set(claim['source_ids']) <= record_sources, f'{rid}: claim source absent from record')
            if claim['status'] == 'conflicting':
                require(len(claim['source_ids']) >= 2 and claim['notes'], f'{rid}: conflict needs both sources and an explanation')
        for bound in record['complexity']:
            require(set(bound['source_ids']) <= record_sources, f'{rid}: complexity source absent from record')
        require(set(record['test_ids']) <= test_ids, f'{rid}: unresolved tests')
    # Ensure structural validation actually rejects three consequential mistakes.
    bad = copy.deepcopy(examples[0])
    bad['claims'][0]['values'] = ['invented_term']
    require(not validator.is_valid(bad), 'Unknown vocabulary was accepted')
    bad = copy.deepcopy(examples[0])
    bad['claims'][0]['source_ids'] = []
    require(not validator.is_valid(bad), 'Unsupported evidence-free positive claim was accepted')
    bad = copy.deepcopy(examples[0])
    bad['claims'][0]['status'] = 'conditional'
    bad['claims'][0]['condition'] = None
    require(not validator.is_valid(bad), 'Conditional claim without condition was accepted')
    screening = read_csv('screening.csv')
    require(len(screening) == len(examples), 'Screening/example counts differ')
    for row, record in zip(screening, examples):
        require(row['record_id'] == record['record_id'], 'Screening/example identity differs')
        supported = {c['dimension']: '|'.join(c['values']) for c in record['claims'] if c['status'] == 'supported'}
        for column in vocabulary.keys() & row.keys():
            require(row[column] == supported.get(column, 'unverified'), f"{row['record_id']}: stale screening field {column}")
    local_count = 0
    if args.check_sources:
        for source in sources:
            if source['local_path']:
                path = ROOT / source['local_path']
                require(path.is_file(), f'Missing source: {path}')
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                require(digest == source['sha256'], f"Source changed since review: {source['id']}")
                local_count += 1
    print(f'Valid: {len(dimensions)} facets, {len(examples)} examples + template, {len(sources)} sources, {len(tests)} test families; 3 negative schema probes rejected; {local_count} local hashes checked.')


if __name__ == '__main__':
    validate()

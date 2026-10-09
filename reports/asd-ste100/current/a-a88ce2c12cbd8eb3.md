# A Unifying Look at Data Structures

- Work ID: `w-a88ce2c12cbd`
- Asset ID: `a-a88ce2c12cbd8eb3`
- Source PDF: `literature/academic-papers-processed/A Unifying Look at Data Structures - Vuillemin.pdf`
- SHA-256: `a88ce2c12cbd8eb3463bf8957dba14aea2a2f2ed7950b093b2a08ce159eda5b5`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Vuillemin uses geometrical combinatorics to derive data structures and algorithms for searching and list manipulation. (PDF p. 1).
- Cartesian trees support two-dimensional searching. Position tournaments adapt these trees to linear lists. (PDF p. 9).

## Objectives

- The author uses representations of n! to show how combinatorial correspondences can guide algorithm design and analysis. (PDF p. 1).

## Arguments

- The author treats bijections between combinatorial representations as algorithms that convert between data structures. (PDF p. 1).
- The author argues that geometric analysis can give simpler and stronger results than direct computational analysis of comparison counts. (PDF p. 7).

## Analysis

- For a random subdiagonal table, the expected number of zero entries is Hn. The expected number of entries on either boundary is 2Hn − 1. (PDF p. 3).
- The insertion analysis assumes a uniformly random result tree and an inserted point chosen uniformly from its n elements. (PDF p. 7).
- The author maps insertion comparison counts to tree-path lengths through a bijection. (PDF p. 7).

## Methods

- INSERT compares the new point with the root. If its y coordinate is smaller, CUT splits the tree at its x coordinate and the new point becomes the root. Otherwise, insertion continues in the appropriate subtree. (PDF p. 7).
- A position tournament stores each list value with its rank, defined as one plus the size of its left subtree. SEARCH compares the requested position with this rank and descends into one subtree. (PDF p. 9).
- EXTRACT finds the requested position and joins its two subtrees with CONS. Extraction from a left subtree decreases the ancestor rank by one. (PDF p. 10).

## Applications

- The author proposes Cartesian trees for searches on plane point sets, including range search, merge, and extraction. (PDF p. 7).
- Position tournaments support positional search, insertion, deletion, list concatenation, and list splitting. (PDF p. 9).
- The author connects binary tournaments with Quicksort, linear lists, and priority queues. (PDF p. 10).

## Optimization

- The author describes pagodas from related work. Their bottom-up merge of tree boundary sequences is more efficient than the paper's top-down method. (PDF p. 10).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- The reported mean number of x-coordinate comparisons for INSERT is 2Hn − 1, where n is the result size. (PDF p. 7).
- The author reports O(log n) average execution time for the position-tournament list primitives. (PDF p. 9).
- SEARCH uses 2(1 + 1/n)Hn − 3 comparisons on average across all list positions. (PDF p. 9).
- The reported mean number of value comparisons during EXTRACT's subtree concatenation is 1 − 2Hn/n + 1/n. (PDF p. 10).

## Limitations and uncertainty

- The insertion bounds depend on the stated random-tree and random-point assumptions. (PDF p. 7).
- The claim that position tournaments are faster on average than other list representations is limited to representations known to the author. (PDF p. 2).

## References

1. Aho, A.V., Hopcroft, J., and Ullman, J.D. The Design and Analysis of Computer Algorithms. Addison-Wesley, Reading, Mass., 1974. (PDF p. 11)
2. Brown, M.R., and Tarjan, R.E. A representation for linear lists with movable f'mgers. In Proc. 10th Ann. ACM Symp. Theory of Comptg., 1978, pp. 19-29. (PDF p. 11)
3. Comtet, L. Advanced Combinatorics. D. Reided Pub. Co., Boston, Mass., 1974. (PDF p. 11)
4. Burge, W.H. An analysis of a tree sorting method and some properties of a set of trees. In Proc. 1st USA-Japan Comptr. Conf., 1972, pp. 372-378. (PDF p. 11)
5. Flajolet, P., Franfon, J., Viennot, G., and Vuillemin, J. Algorithmique et combinatoire des arbres et permutations. To appear (1981). (PDF p. 11)
6. Flajolet, P., Frangon, J., and Vuillemin, J. Sequence of operation analysis for dynamic data structures. 3".Algorithms. To appear (1980). (PDF p. 11)
7. Foata, D., and Schutzenberger, M.P. Theorie g~omCtrique des polynCmes Euleriens. Lecture Notes in Mathematics, No. 138, Springer-Verlag, Berlin, 1970. (PDF p. 11)
8. Foata, D., and Strehl, V. Rearrangements of the symmetric group and enumerative properties of the tangent and secant numbers. Math. Zamet. 137 (1974), 256-264. (PDF p. 11)
9. Frangan, J. Arbres binaires de recherche, propriCtCs combinatoires et applications. RA I R O Informatique Thdorique 10 (1976), 35-50. (PDF p. 11)
10. Fran~on, J., Viennot, G., and VuiUemin, J. Description et analyse d'une reprCsentation pefformante des files de prioritC. Rep. 12, Lab. d'Informatique, Orsay, France; also in Proc. 19th Ann. ACM Syrup. on Foundations of Comptr. Sci., 1978, pp. 1-7. (PDF p. 11)
11. Guibas, L., Creight, E.M.M., Plass, M.F., and Roberts, J.R. A new representation for linear lists. In Proc. 9th Ann. ACM Syrup. Theory of Comptg., 1977, pp. 49-60. (PDF p. 11)
12. Hoare, C.A.R. Quicksort. Comptr. J. 5, 1 (1962), 10--15. (PDF p. 11)
13. Knuth, D.E. The Art of Computer Programming, Vol. 3: Sorting and Searching. Addison-Wesley, Reading, Mass., 1973. (PDF p. 11)
14. Sedgewick, R. Quicksort. Rep. STAN-CS-75-492, Dept. Comptr. Sci., Stanford Univ., Stanford, Calif,, May 1975. (PDF p. 11)
15. Stephenson, C.J. A method for constructing binary search trees by making insertions at the root. Rep. RC 6298, IBM Thomas J. Watson Res. Ctr., Yorktown Heights, N.Y., 1976. (PDF p. 11)
16. Viennot, G. Quelques algorithmes de permutations. AstCrique 38-39, Societ6 MathCmatique de France, 1976, pp. 275-293. Professional Activities Calendar of Events ACM's calendar policy is to list open computer science meetings that are held on a not-for-profit Basis, Not included in the calendar are educational seminars, institutes, and courses. Submittals should be substantiated with name of the sponsoring orga- nization, fee schedule, and chairman's name and full address. One telephone number contact for those interested in attending a meeting will be given when a number is specified for this purpose. All requests for ACM sponsorship or cooperation should be addressed to Chairman, Conferences and Symposia Committee, Seymour J. Wolfson, 643 MacKenzie Hall, Wayne State University, Detroit, MI 48202, with a copy to Louis Flora, Conference Coordinator, ACM Headquarters, 1133 Avenue of the Americas, New York,NY 10036; 212 265-6300. For European events, a copy of the request should also be sent to the European Representative. Tech- nical Meeting Request Forms for this purpose can be obtained from ACM Headquarters or from the European Regional Representative. Lead time should include 2 months (3 months if for Europe) for processing of the request, plus the necessary months (minimum 3) for any publicity to appear in Communications. • This symbol indicates that the Conferences and Symposia Committee has given its approval for ACM sponsorship or cooperation. In this issue the calendaris given to November 1981. New Listings are shownfirst," they willappear next month as PrevtousListings. NEW LISTINGS 15-17 April 1980 • Annual Conference on Computer Graphics, De- troit, Mich. Sponsor: Engineering Society of Detroit in cooperation with ACM. Conf. chin: Fred Lan- ghorst, Transportation Systems Center, General Mo- tors Technical Center, Warren, MI 48090; 313 575- 8311. 29-30 April 1980 Sixth Illinois Conference on Medical Informa- tion Systems, Champaign, Ill. Sponsors: University of Illinois, Regional Health Resource Center, Society for Advanced Medical Systems, Society for Com- puter Medicine, University of Missouri Health Care 239 Technology Center. Contact: Saundra Wheeler, 1408 W. University, Urbana, IL 61801. (PDF p. 11)
17. April 1980 Capacity Planning and Shop Floor Control, Syr- acuse, N.Y. Sponsors: ACM Syracuse Chapter, American Production and InventoryControl Society Syracuse Chapter. Contact: Michael Busse, Anaren Microwave Inc., 185 Ainsley Dr., Syracuse, NY 13205 or Hamilton Armstrong, Carrier Corp., Box 4895, Syracuse, NY 13221. 6-10 May 1980 Canadian Association for Information Science Annual Conference, Toronto, Ont., Canada. Sponsor: CAIS. Contact: Ilse Cockburn, 36 Brookdale Ave., Toronto, Ontario, Canada M5M IP3. 15-16 May 1980 NYU Symposium on Distributed Processing Practice, New York City. Sponsor: Graduate School of Business Administration of New York University. Contact: CA1S Dept., 700 Merrill Hall, 90 Trinity Place, New York, NY 10006; 212 285-6120. 3-6 June 1980 International Conference on Boundary and In- terior Layers--Computational and Asymptotic Methods (BAIL I), Dublin, Ireland. Sponsor: Nu- merical Analysis Group. Contact: BAIL I Confer- ence, 39 Trinity College, Dublin 2, Ireland. 16-19 June 1980 Thirteenth Annual Conference of Association of Small Computer Users in Education, University of Tennessee, Martin. Sponsor: ASCUE. Contact: James Westmoreland, Computer Center, University of Tennessee, Martin, TN 38238; 901 587-7891. 26-27 June 1980 • ACM SIGPCR Seventeenth Annual Computer Personnel Research Conference, Boca Raton, Fla. OnSor:ACM SIGPCR. Conf. chm: Elias M. Awad, liege of Business and Organizational Sciences, Florida International University, Miami, FL 33199; 305 552-2791. (PDF p. 11)
18. June 1980 Panel on Software Metrics, Washington, D.C. Sponsors: Yale University and Office of Naval Re- search. Contact: ONR Software Metrics Panel, Attn. Alan J. Perlis, Computer Science Dept., Yale Uni- versity, 2158 Yale Station, New Haven, CT 06520. 19-21 August 1980 • National Artificial Intelligence Conference, Palo Alto, Calif. Sponsor: American Association for Ar- tificial Intelligence in cooperation with ACM SI- GART. Conf. chm: J. Marty Tenenbaum, SRI In- Communications of the ACM ternational, 333 Ravenswood Ave., Menlo Park, CA 94025; 415 326-6200 x4167. 3-5 September 1980 19th Annual Lake Arrowhead Workshop on Office Information Systems, near Los Angeles, Calif. Sponsor: IEEE-CS. Workshop co-chm: Clarence A. Ellis and Gary J. Nutt, Xerox PARC, 3333 Coyote Hill Road, Palo Alto, CA 94304. 15-17 October 1980 V ICCRE, Fifth International Conference on Computers in Chemical Research and Education, Toyohashi, Japan (a post congress symposium of Seventh International CODATA Conference, Kyoto, Oct. 8-11). Contact: S. Sasaki, School of Materials Science, Toyohashi University of Tech- nology, Tempaku, Toyohashi, Japan 440. 2-5 November 1980 Fourth Annual Symposium on Computer Appli- cations in Medical Care, Washington, D.C. Sponsor: The George Washington University Medical Center. Prog. chm: Joseph T. O'Neill, National Center for Health Services Research, Center Building, Room 8- 30 #1, 3700 East-West Highway, Hyattsville, MD 20782; 301 436-8946. (PDF p. 11)
19. November-2 December 1980 • Micro 13--13th Annual Workshop on Micropro- grannning, Colorado Springs, Colo. Sponsors: ACM SIGMICRO, IEEE-CS. Conf. chin: G.R. Johnson, Dept. of Engineering Science, Colorado State Uni- versity, Fort Collins, CO 80523; 303 491-7585. 3-8 December 1980 • 1980 Winter Simulation Conference, Orlando, Fla. Sponsors: ACM SIGSIM, ORSA, TIMS, AIEE, SCS, U.S. Dept. of Energy. Conf. chm: Paul F. Roth, U.S. Dept. of Energy, Mail Stop 4530, 12th and Penn, Washington, DC 20461; 202633-9629. 3-5 February 1981 • Fifth Berkeley Workshop on Distributed Data Management and Computer Networks, Emeryville, Calif. Sponsor: Lawrence Berkeley Laboratory in cooperation with ACM. Conf. chm: Rowland R. Johnson, Lawrence Berkeley Laboratory, University of California, Berkeley, CA 94720; 415 486-6321. 19-22 April 1981 • Computing for Development, Bangkok, Thai- land. Sponsors: Carl Duisberg Gesellschaft, Asian Institute of Technology in cooperation with ACM SIGBDP, SIGCAS, SIGMOD, SIGSIM. Conf. chm: M. Nawaz Sharif, Div. of Computer Applications, Asian Institute of Technology, P.O. Box 2754, Bang- kok, Thailand. (Calendar continuedon p. 242) April 1980 Volume 23 Number 4 (PDF p. 11)

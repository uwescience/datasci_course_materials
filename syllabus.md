**Part 0: Introduction**

**Data science articulated, data science examples, history and context, technology landscape **

_Readings_

- (example) Yong-Yeol Ahn, Sebastian E. Ahnert, James P. Bagrow, Albert-László Barabási,  [Flavor network and the principles of food pairing](http://www.nature.com/srep/2011/111215/srep00196/full/srep00196.html), Scientific Reports 1, Article number: 196 doi:10.1038/srep00196
- (example) Acerbi A, Lampos V, Garnett P, Bentley RA (2013)  [The Expression of Emotions in 20th Century Books](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0059030). PLoS ONE 8(3): e59030. doi:10.1371/journal.pone.0059030
- (example)  [Google Flu Trends](http://www.google.org/flutrends/us/#US) (plus: David Wagner,  [Google Flu Trends Wildly Overestimated This Year's Flu Outbreak](http://www.theatlanticwire.com/technology/2013/02/google-flu-trends-wildly-overestimated-years-flu-outbreak/62113/), Atlantic Wire, February 13, 2013)
- [Eigenfactor](http://www.eigenfactor.org/), and  [publications](http://www.eigenfactor.org/papers.php)
- (example)  [L'Aquila quake: Italy scientists guilty of manslaughter](http://www.bbc.co.uk/news/world-europe-20025626), BBC
- [Drew Conway's Venn Diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram)_ _
- _Mike Loukides, _ [_What is data science?_](http://radar.oreilly.com/2010/06/what-is-data-science.html)_, O'Reilly Radar, 2010_
- _Mike Driscoll, "_ [_The Seven Secrets of Successful Data Scientists_](http://www.dataspora.com/2010/08/the-seven-secrets-of-successful-data-scientists/)_", Dataspora_
- [Origins of "Volume, Velocity, Variety"](http://blogs.gartner.com/doug-laney/deja-vvvue-others-claiming-gartners-volume-velocity-variety-construct-for-big-data/)_ _
- [eScience: The Fourth Paradigm](http://research.microsoft.com/en-us/collaboration/fourthparadigm/) (Foreward and Introduction, pages xi - xxxi; Gray's Laws, pages 5-12)
- Chris Anderson,   ["The End of Theory: The Data Deluge Makes the Scientific Method Obsolete"](http://www.wired.com/science/discoveries/magazine/16-07/pb_theory) , Wired magazine, 2008
- [Responses to Chris Anderson](http://www.edge.org/discourse/the_end_of_theory.html), 2008

**Part 1: Data Manipulation, at Scale**

**Databases and the relational algebra**

_Readings_

- [How Vertica Was the Star of the Obama Campaign, and Other Revelations](http://citoresearch.com/data-science/how-vertica-was-star-obama-campaign-and-other-revelations)
- E. F. Codd,  [1981 Turing Award Lecture, "](http://amturing.acm.org/award_winners/codd_1000892.cfm)  [Relational Database: ](http://amturing.acm.org/award_winners/codd_1000892.cfm)  [A Practical Foundation for Productivity"](http://amturing.acm.org/award_winners/codd_1000892.cfm), 1981 (Think about which arguments from this short piece are still relevant today.)
- [Advanced] Cohen et al. ["MAD Skills: New Analysis Practices for Big Data"](http://db.cs.berkeley.edu/papers/vldb09-madskills.pdf), 2009
- [Advanced] Erik Meijer, Gavin Bierma  [co-Relational Model of Large Shared Data Banks](http://queue.acm.org/detail.cfm?id=1961297), Communications of the ACM, 2011

**MapReduce, Hadoop, relationship to databases, algorithms, extensions, language; key-value stores and NoSQL; tradeoffs of SQL and NoSQL **

_Readings_

- Ullman, Rajaraman,  [Mining of Massive Datasets](http://infolab.stanford.edu/~ullman/mmds.html), Chapter 2
- Stonebraker et al., " [MapReduce and Parallel DBMS's: Friends or Foes?](http://database.cs.brown.edu/papers/stonebraker-cacm2010.pdf)", Communications of the ACM, January 2010.
- Dean and Ghemawat, " [MapReduce: A Flexible Data Processing Too](http://cacm.acm.org/magazines/2010/1/55744-mapreduce-a-flexible-data-processing-tool/fulltext)l", _Communications of the ACM, _January 2010.
- Rick Cattell, " [Scalable SQL and NoSQL Data Stores](http://www.sigmod.org/publications/sigmod-record/1012/pdfs/04.surveys.cattell.pdf)", _SIGMOD Record_, December 2010 (39:4)
- Michael Armbrust, Reynold S. Xin, Cheng Lian, Yin Huai, Davies Liu, Joseph K. Bradley, Xiangrui Meng, Tomer Kaftan, Michael J. Franklin, Ali Ghodsi, and Matei Zaharia. 2015. [Spark SQL: Relational Data Processing in Spark](http://people.csail.mit.edu/matei/papers/2015/sigmod_spark_sql.pdf). SIGMOD '15

**Data cleaning, entity resolution, data integration, information extraction**

_Readings_

- Elmagarmid, et. al. "Duplicate Record Detection:  A Survey"
- Koudas, et. al. "Record Linkage:  Similarity Measures and Algorithms"

**Part 2: Analytics**


**Basic statistical modeling, experiment design**

 _Readings_

- Chapter 3 of  A Handbook of Statistical Analyses Using R
- [Gregory Park on overfitting to the leaderboard in a Kaggle Competition](http://blog.kaggle.com/2012/07/06/the-dangers-of-overfitting-psychopathy-post-mortem/)

**Introduction to Machine Learning, supervised learning, decision trees/forests, simple nearest neighbor**

_Readings_

- Xindong Wu et al.,  [Top 10 Algorithms in Data Mining, Knowledge and Information Systems](http://www.cs.uvm.edu/~icdm/algorithms/index.shtml), 14(2008), 1: 1-37.  (read C4.5)
- Ullman, Rajaraman,   [Mining of Massive Datasets](http://infolab.stanford.edu/~ullman/mmds/book.pdf) , Chapter 1
- Pedro Domingos,  [A Few Useful Things to Know about Machine Learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf), CACM 55(10), 2012

**Unsupervised learning: k-means, multi-dimensional scaling**

_Readings_

- Xindong Wu et al.,  [Top 10 Algorithms in Data Mining, Knowledge and Information Systems](http://www.cs.uvm.edu/~icdm/algorithms/index.shtml), 14(2008), 1: 1-37.  (read k-means)

**Part 3: Interpreting and Communicating Results**

**Visualization, visual data analytics **

_Readings (well, watchings)_

- Hans Rosling,  [The Joy of Stats](http://www.gapminder.org/videos/the-joy-of-stats/)
- Pat Hanaran,  [Tools for Data Enthusiasts](http://vimeo.com/50723101)
- Jeffrey Heer, Michael Bostock, Vadim Ogievetsky,  [A Tour through the Visualization Zoo](http://queue.acm.org/detail.cfm?id=1805128), Communications of the ACM, Volume 53 Issue 6, June 2010

**Ethics, privacy**

- Howard Wen, " [Big Ethics for Big Data](http://strata.oreilly.com/2012/06/ethics-big-data-business-decisions.html)", O'Reilly Media
- John Markoff, New York Times,  [Unreported Side Effects of Drugs Are Found Using Internet Search Data](http://www.nytimes.com/2013/03/07/science/unreported-side-effects-of-drugs-found-using-internet-data-study-finds.html?_r=0), March 13, 2013
- Mike Loukides,  [Data Skepticism](http://strata.oreilly.com/2013/04/data-skepticism.html), O'Reilly Media, April 2013

**Part 4: Special Topics**

- Graph Analytics: PageRank, community detection, recursive queries, iterative processing
- Guest Lecture: Datameer
- Guest Lecture: Wibidata

_Readings _

- Dan Mckinley,  [Whom the Gods Would Destroy, they First Give Real-Time Analytics](http://mcfunley.com/whom-the-gods-would-destroy-they-first-give-real-time-analytics)
- Joseph Wilk, [ Latent Semantic Analysis in Python](http://blog.josephwilk.net/projects/latent-semantic-analysis-in-python.html)

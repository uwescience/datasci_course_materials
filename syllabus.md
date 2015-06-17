# Introduction to Data Science

This two-day accelerated course is intended to give graduate students in computer science an overview of the topics associated with data science.  It provides an overview of key topics in scalable data management, selected topics in statistics not always taught in introductory stats classes, a treatment of key topics and algorithms in machine learning, an introduction to the field of visualization research, and an overview of graph analytics. 

# Day 1: Scalable Data Management 

## Introduction 

- Appetite whetting and context (10 min)
- Course goals and logistics (10 min)
- Twitter Sentiment Analysis (1 hour)

*Readings*

- (example) Yong-Yeol Ahn, Sebastian E. Ahnert, James P. Bagrow, Albert-Laszlo Barabasi,  [Flavor network and the principles of food pairing](http://www.nature.com/srep/2011/111215/srep00196/full/srep00196.html), Scientific Reports 1, Article number: 196 doi:10.1038/srep00196
- (example) Acerbi A, Lampos V, Garnett P, Bentley RA (2013)  [The Expression of Emotions in 20th Century Books](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0059030). PLoS ONE 8(3): e59030. doi:10.1371/journal.pone.0059030
- (example)  [Google Flu Trends](http://www.google.org/flutrends/us/#US) (plus: David Wagner,  [Google Flu Trends Wildly Overestimated This Year's Flu Outbreak](http://www.theatlanticwire.com/technology/2013/02/google-flu-trends-wildly-overestimated-years-flu-outbreak/62113/), Atlantic Wire, February 13, 2013)
- (example)  [L'Aquila quake: Italy scientists guilty of manslaughter](http://www.bbc.co.uk/news/world-europe-20025626), BBC
- [Drew Conway's Venn Diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram)
- Mike Loukides, [What is data science?](http://radar.oreilly.com/2010/06/what-is-data-science.html), O'Reilly Radar, 2010_
- [Origins of "Volume, Velocity, Variety"](http://blogs.gartner.com/doug-laney/deja-vvvue-others-claiming-gartners-volume-velocity-variety-construct-for-big-data/)_ _
- Dan Mckinley,  [Whom the Gods Would Destroy, they First Give Real-Time Analytics](http://mcfunley.com/whom-the-gods-would-destroy-they-first-give-real-time-analytics)
- Howard Wen, " [Big Ethics for Big Data](http://strata.oreilly.com/2012/06/ethics-big-data-business-decisions.html)", O'Reilly Media
- John Markoff, New York Times,  [Unreported Side Effects of Drugs Are Found Using Internet Search Data](http://www.nytimes.com/2013/03/07/science/unreported-side-effects-of-drugs-found-using-internet-data-study-finds.html?_r=0), March 13, 2013
- Mike Loukides,  [Data Skepticism](http://strata.oreilly.com/2013/04/data-skepticism.html), O'Reilly Media, April 2013
- [eScience: The Fourth Paradigm](http://research.microsoft.com/en-us/collaboration/fourthparadigm/) (Foreward and Introduction, pages xi - xxxi; Gray's Laws, pages 5-12)
- Chris Anderson,   ["The End of Theory: The Data Deluge Makes the Scientific Method Obsolete"](http://www.wired.com/science/discoveries/magazine/16-07/pb_theory) , Wired magazine, 2008
- [Responses to Chris Anderson](http://www.edge.org/discourse/the_end_of_theory.html), 2008

## Databases and the relational algebra

- From Data Models to Databases (10 min)
- Motivation for Relaional Algebra (10 min)
- Relational Algebra Introduction (10 min)
- RA Operators (30 min)
- Adapting SQL for Data Science (10 min)
- Physical Optimization (10 min)
- Logical Data Independence (20 min)
- Assignment: SQL Analytics (30 min)

*Readings*

- [How Vertica Was the Star of the Obama Campaign, and Other Revelations](http://citoresearch.com/data-science/how-vertica-was-star-obama-campaign-and-other-revelations)
- E. F. Codd,  [1981 Turing Award Lecture, "](http://amturing.acm.org/award_winners/codd_1000892.cfm)  [Relational Database: ](http://amturing.acm.org/award_winners/codd_1000892.cfm)  [A Practical Foundation for Productivity"](http://amturing.acm.org/award_winners/codd_1000892.cfm), 1981 (Think about which arguments from this short piece are still relevant today.)
- [Advanced] Cohen et al. ["MAD Skills: New Analysis Practices for Big Data"](http://db.cs.berkeley.edu/papers/vldb09-madskills.pdf), 2009
- [Advanced] Erik Meijer, Gavin Bierma  [co-Relational Model of Large Shared Data Banks](http://queue.acm.org/detail.cfm?id=1961297), Communications of the ACM, 2011

## MapReduce

- MapReduce Abstractions and model (10 min)
- Examples: Text, relational join, matrix multiply (30 min)
- Implementation (15 min)
- Comparison with Databases (30 min)
- Assignment: MR Algorithms (1 hour)

*Readings*

- Dean and Ghemawat, " [MapReduce: A Flexible Data Processing Too](http://cacm.acm.org/magazines/2010/1/55744-mapreduce-a-flexible-data-processing-tool/fulltext)l", _Communications of the ACM, _January 2010.
- Ullman, Rajaraman,  [Mining of Massive Datasets](http://infolab.stanford.edu/~ullman/mmds.html), Chapter 2
- Stonebraker et al., " [MapReduce and Parallel DBMS's: Friends or Foes?](http://database.cs.brown.edu/papers/stonebraker-cacm2010.pdf)", Communications of the ACM, January 2010.

## NoSQL

- Introduction (10 min)
- Eventual Consistency (20 min)
- Examples: Memcached, Dynamo, BigTable, MongoDB, Other Google Systems (1 hour)
- NoSQL Response (10 min)
- Assignment: Graph Processing with Pig on AWS (Optional)

*Readings*

- Rick Cattell, " [Scalable SQL and NoSQL Data Stores](http://www.sigmod.org/publications/sigmod-record/1012/pdfs/04.surveys.cattell.pdf)", _SIGMOD Record_, December 2010 (39:4)
- Michael Armbrust, Reynold S. Xin, Cheng Lian, Yin Huai, Davies Liu, Joseph K. Bradley, Xiangrui Meng, Tomer Kaftan, Michael J. Franklin, Ali Ghodsi, and Matei Zaharia. 2015. [Spark SQL: Relational Data Processing in Spark](http://people.csail.mit.edu/matei/papers/2015/sigmod_spark_sql.pdf). SIGMOD '15
- Data cleaning (not covered in lectures)
  - Elmagarmid, et. al. "Duplicate Record Detection:  A Survey"
  - Koudas, et. al. "Record Linkage:  Similarity Measures and Algorithms"

# Day 2: Analytics and Visualization

## Cherry-picked Statistics Topics

- Experimental Design (20 min)
- Multiple Hypothesis Testing (20 min)
- Permutation Methods (20 min)

*Readings*
- Chapter 3 of  A Handbook of Statistical Analyses Using R
- [Gregory Park on overfitting to the leaderboard in a Kaggle Competition](http://blog.kaggle.com/2012/07/06/the-dangers-of-overfitting-psychopathy-post-mortem/)

## Machine Learning Tour

- Introduction (15 min)
- Rules (15 min)
- Trees (20 min)
- Overfitting (10 min)
- Evaluation (10 min)
- Ensembles, Bagging, Boosting (10 min)
- Random Forests (10 min)
- Gradient Descent (30 min)
- K-means, DBSCAN (15 min)

*Readings*

- Xindong Wu et al.,  [Top 10 Algorithms in Data Mining, Knowledge and Information Systems](http://www.cs.uvm.edu/~icdm/algorithms/index.shtml), 14(2008), 1: 1-37.  (read C4.5)
- Ullman, Rajaraman,   [Mining of Massive Datasets](http://infolab.stanford.edu/~ullman/mmds/book.pdf) , Chapter 1
- Pedro Domingos,  [A Few Useful Things to Know about Machine Learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf), CACM 55(10), 2012
- Xindong Wu et al.,  [Top 10 Algorithms in Data Mining, Knowledge and Information Systems](http://www.cs.uvm.edu/~icdm/algorithms/index.shtml), 14(2008), 1: 1-37.  (read k-means)


## Visualization

- Intro (10 min)
- Types, Dimensions (20 min)
- Encodings (10 min)
- Perception (20 min)
- Assignment: D3 Tutorial

*Readings*

  - Hans Rosling,  [The Joy of Stats](http://www.gapminder.org/videos/the-joy-of-stats/)
  - Pat Hanaran,  [Tools for Data Enthusiasts](http://vimeo.com/50723101)
  - Jeffrey Heer, Michael Bostock, Vadim Ogievetsky,  [A Tour through the Visualization Zoo](http://queue.acm.org/detail.cfm?id=1805128), Communications of the ACM, Volume 53 Issue 6, June 2010

## Graph Analytics

- Structure (20 min)
- Traversal (20 min)
- Patterns (20 min)
- PageRank (10 min)


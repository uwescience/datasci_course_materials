register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--- filter when cse344-test-file
--- filter_subject = filter ntriples by subject matches '.*business.*';
--- filter when btc-2010-chunk-000
filter_subject = filter ntriples by subject matches '.*rdfabout\\.com.*';

copy_filter = foreach filter_subject generate $0 as subject2,$1 as predicate2,$2 as object2;

--- join when cse344-test-file
--- object_join_subject = join filter_subject by subject, copy_filter by subject2;
--- when btc-2010-chunk-000
object_join_subject = join filter_subject by object, copy_filter by subject2;

--- Remove duplicate tuples from the result of the join
dist_join = distinct object_join_subject;

-- store the results in the folder /user/hadoop/prob2B-results
store dist_join into '/user/hadoop/prob3-results' using PigStorage();


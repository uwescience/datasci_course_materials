register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the subjects out (because group by produces a tuple of each subject
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_subjects = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

--- group the count_by_subjects by the count
counts = group count_by_subjects by (count) PARALLEL 50;

--- count the total number of subjects associated with each particular count.
count_by_counts = foreach counts generate flatten($0) as xaxis, COUNT($1) as yaxis PARALLEL 50;

-- store the results in the folder /user/hadoop/prob2A-results
store count_by_counts into '/user/hadoop/prob2A-results' using PigStorage();


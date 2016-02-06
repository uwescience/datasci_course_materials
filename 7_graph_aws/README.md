Instructions on how to run example.pig.

== STEP 1

Importing the myudfs.jar file in pig. You need this because example.pig uses the function RDFSplit3(...) which is defined in myudfs.jar:

OPTION 1: Do nothing. example.pig is already configured to read myudfs.jar from S3, through the line:

register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

OPTION 2: Do-it-yourself; run this on your local machine:

cd pigtest
ant

This should create the file myudfs.jar

Next, modify example.pig to:

register ./myudfs.jar

Next, after you start the AWS cluster, copy myudfs.jar to the AWS Master Node (see hw6-awsusage.html).

== STEP 2

Start an AWS Cluster (see awsinstructions.md), start pig interactively, and cut and paste the content of example.pig. I prefer to do this line by line

Note: The program may appear to hang with a 0% completion time... Check the Hadoop monitor or cluster details page. You should see a MapReduce job running with some non-zero progress.

Also note that the script will generate more than one MapReduce job.

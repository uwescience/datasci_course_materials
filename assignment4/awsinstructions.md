## Setting up your AWS account 

Amazon will ask you for your credit card information during the
setup process. You will be charged for using their services. You should not have to spend more than 5-10 dollars.

1. Go to [http://aws.amazon.com/](http://aws.amazon.com/ "Link: http://aws.amazon.com/")
and sign
up:
  
  1. You may sign in using your existing Amazon account or you can create a
new account by selecting "I am a new user."
  2. Enter your contact information and confirm your acceptance of the AWS
Customer Agreement.
  3. Once you have created an Amazon Web Services Account, you may need to
accept a telephone call to verify your identity. Some students have used
[Google Voice](https://www.google.com/voice "Link: https://www.google.com/voice")successfully if you don't have or don't want to give a
mobile number. You need Access Identifiers to make valid web service requests.
2. Go to [http://aws.amazon.com/](http://aws.amazon.com/ "Link: http://aws.amazon.com/")
and sign
in. You need to double-check that your account is signed up for three of
their services: Simple Storage Service (S3), Elastic Compute Cloud (EC2),
and Amazon Elastic MapReduce by clicking [here](https://aws-portal.amazon.com/gp/aws/manageYourAccount "Link: https://aws-portal.amazon.com/gp/aws/manageYourAccount") -- you should see "Services You're Signed Up For" under "Manage
Your Account".

## Setting up an EC2 key pair

Go to [AWS security credentials page](https://portal.aws.amazon.com/gp/aws/securityCredentials "Link: https://portal.aws.amazon.com/gp/aws/securityCredentials") and
make sure that you see a key under the access key, if not just click Create
a new Access Key.

To connect to an Amazon EC2 node, such as the master nodes for the Hadoop
clusters you will be creating, you need an SSH key pair. To create and
install one, do the following:

1. After setting up your account, follow
[Amazon's instructions](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/generating-a-keypair.html) to create a key pair. Follow the instructions
in section "Having AWS create the key pair for you," subsection "AWS Management
Console." (Don't do this in Internet Explorer, or you might not be able
to download the .pem private key file.)
2. Download and save the .pem private key file to disk. We will reference
the .pem file as `</path/to/saved/keypair/file.pem>`
in
the following instructions.
3. Make sure only you can access the .pem file. If you do not change the
permissions, you will get an error message later: 
    
    $ chmod 600 </path/to/saved/keypair/file.pem>

4. Note: This step will NOT work on Windows 7 with cygwin. Windows 7 does
not allow file permissions to be changed through this mechanism, and they
must be changed for ssh to work. So if you must use Windows, you should
use [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) as
your ssh client. In this case, you will further have to transform this
key file into PuTTY format. For more information go to [http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html "Link: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html") and
look under "Private Key Format."

## Starting an AWS Cluster and running Pig Interactively

To run a Pig job on AWS, you need to start up an AWS cluster using the
[Web Management Console](https://console.aws.amazon.com/elasticmapreduce/home "Link: https://console.aws.amazon.com/elasticmapreduce/home") and connect to the Hadoop master node. Follow
the steps below. 
To set up and connect to a pig cluster, perform the following steps:

  1. Go to [http://console.aws.amazon.com/elasticmapreduce/home](http://console.aws.amazon.com/elasticmapreduce/home "Link: http://console.aws.amazon.com/elasticmapreduce/home") and
sign in.
  2. Click the "Amazon Elastic MapReduce" tab.
  3. Click on "Create cluster" in the EMR menu, and from there stay in the quick options and select in Applications "Core Hadoop" which should have everything you need. You can disable logging. Previous version c1.medium or m1.medium are acceptable for this exercise. Make sure you select your SSH keypair before clicking "Create cluster" otherwise you won't be able to SSH to your cluster. 
  4. Go to https://console.aws.amazon.com/ec2/v2/, Networks and security, security groups and add to the group containing the master an inbound rule allowing ssh from anywhere.
  5. In the cluster details, next to Master public DNS, click on SSH to have the command to run from the command line to connect to the cluster
  6. Once you connect successfully, just type 
    
     **$ pig**

  7. Now you should have a Pig prompt:
  

      **grunt>**
    

In this quiz we will use pig only interactively. (The alternative
is to have pig read the program from a file.)
  
This is the interactive mode where you type in pig queries. Here you will
cut and paste `example.pig`. You are now ready to return to the
quiz.
  
  
Other useful information:
  * For the first job you run, Hadoop will create the output directory for
you automatically. But Hadoop refuses to overwrite existing results. So
you will need to move your prior results to a different directory before
re-running your script, specify a different output directory in the script,
or delete the prior results altogether.
  
To see how to perform these tasks and more, see ["Managing the results of your Pig queries"](#managingresults "Link: #managingresults") below.
  * To exit pig, type `quit` at the `grunt>` promt. To
terminate the ssh session, type `exit` at the unix prompt: after
that you must terminate the AWS cluster (see next).
  * To kill a pig job type CTRL/C while pig is running.This kills pig only:
after that you need to kill the hadoop job. We show you how to do this
below.
  

## Monitoring Hadoop jobs

These instructions are available on the AWS control center, from the cluster details page (link next to *Connections*, under *Enable Web Connection*)

In summary:

###  Open an SSH Tunnel to the Amazon EMR Master Node

From the terminal, type
 
> `ssh -i </path/to/saved/keypair/file.pem>  -ND 8157 hadoop@<your instance>`

The SSH window will appear to hang, without any output; this
is normal as SSH has not started a shell on the master node, but just created
the tunnel over which proxied traffic will run.

### Install and configure FoxyProxy

1. Download and isntall FoxyProxy
2. Using a text editor create a file named foxyproxy-settings.xml containing the following:

```
<?xml version="1.0" encoding="UTF-8"?>
<foxyproxy>
    <proxies>
        <proxy name="emr-socks-proxy" id="2322596116" notes="" fromSubscription="false" enabled="true" mode="manual" selectedTabIndex="2" lastresort="false" animatedIcons="true" includeInCycle="true" color="#0055E5" proxyDNS="true" noInternalIPs="false" autoconfMode="pac" clearCacheBeforeUse="false" disableCache="false" clearCookiesBeforeUse="false" rejectCookies="false">
            <matches>
                <match enabled="true" name="*ec2*.amazonaws.com*" pattern="*ec2*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*ec2*.compute*" pattern="*ec2*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="10.*" pattern="http://10.*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*10*.amazonaws.com*" pattern="*10*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*10*.compute*" pattern="*10*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*.compute.internal*" pattern="*.compute.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*.ec2.internal*" pattern="*.ec2.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            </matches>
            <manualconf host="localhost" port="8157" socksversion="5" isSocks="true" username="" password="" domain="" />
        </proxy>
    </proxies>
</foxyproxy> 

```

3. Click the FoxyProxy icon in the toolbar and select Options.  Click File > Import Settings.  Browse to foxyproxy-settings.xml, select it, and click Open.  To confirm that you wish to overwrite current settings with those stored in the new file, click Yes.
4. Beside the FoxyProxy Standard add-on, click Options.  In the FoxyProxy Standard dialog, for Select Mode, choose Use proxies based on their predefined patterns and priorities.

You can now connect to your instance from your browser by typing its address in the FireFox/Chrome URL bar. The list of the ports are available ["Here"](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-web-interfaces.html).



> The job tracker enables you to see what MapReduce jobs are executing in
> your cluster and the details on the number of maps and reduces that are
> running or already completed.
> 
> Note that, at this point in the instructions, you will not see any MapReduce
> jobs running but you should see that your cluster has the capacity to run
> a couple of maps and reducers on your one instance.
> 
> The HDFS manager gives you more low-level details about your cluster and
> all the log files for your jobs. 

## Killing a Hadoop Job

Later, in the assignment, we will show you how to launch MapReduce jobs
through Pig. You will basically write Pig Latin scripts that will be translated
into MapReduce jobs (see lecture notes). Some of these jobs can take a
long time to run. If you decide that you need to interrupt a job before
it completes, here is the way to do it:

If you want to kill pig, you first type CTRL/C, which kills pig only.
Next, kill the hadoop job, as follows. From the job tracker interface find
the hadoop `job_id`, then type:

> `% hadoop job -kill job_id`
> 

You do not need to kill any jobs at this point.

However, you can now exit pig (just type "quit") and exit your ssh session.
You can also kill the SSH SOCKS tunnel to the master node.

## Terminating an AWS cluster

When you are done running Pig scripts, make sure to **ALSO** terminate
your job flow. This is a step that you need to do **in addition to **stopping
pig and Hadoop (if necessary) above.

This step shuts down your AWS cluster:
  1. Go to the [Management Console.](https://console.aws.amazon.com/elasticmapreduce/home)
  2. Select the job in the list.
  3. Click the Terminate button (it should be right below "Your Elastic MapReduce
Job Flows").
  4. Wait for a while (may take minutes) and recheck until the job state becomes
TERMINATED.

**Pay attention to this step**. If you fail to terminate
your job and only close the browser, or log off AWS, your AWS will continue
to run, and AWS will continue to charge you: for hours, days, weeks, and
when your credit is exhausted, it chages your creditcard. Make sure you
don't leave the console until you have confirmation that the job is terminated.

You can now shut down your cluster.

## 

## Checking your Balance 

Please check your balance regularly!!!
  1. Go to the [Management Console.](https://console.aws.amazon.com/elasticmapreduce/home)
  2. Click on your name in the top right corner and select "Account Activity".
  3. Now click on "detail" to see any charges < $1\.

To avoid unnecessary charges, terminate your job flows when you are not
using them.

**USEFUL**: AWS customers can now use **billing alerts** to
help monitor the charges on their AWS bill. You can get started today by
visiting your [Account Activity page](https://aws-portal.amazon.com/gp/aws/developer/account/index.html) to enable monitoring of your charges.
Then, you can set up a billing alert by simply specifying a bill threshold
and an e-mail address to be notified as soon as your estimated charges
reach the threshold. 

## Managing the results of your Pig queries

For the next step, you need to restart a new cluster as follows. Hopefully,
it should now go very quickly:
  * Start a new cluster with one instance.
  * Start a new interactive Pig session (through grunt)
  * Start a new SSH SOCKS tunnel to the master node (if you are using your
own browser)

We will now get into more details about running Pig scripts.

Your pig program stores the results in several files in a directory. You
have two options: (1) store these files in the Hadoop File System, or (2)
store these files in S3\. In both cases you need to copy them to your local
machine.

### 1\. Storing Files in the Hadoop File System

This is done through the following pig command (used in `example.pig`):

     store count_by_object_ordered into '/user/hadoop/example-results' using PigStorage();

Before you run the pig query, you need to (A) create the /user/hadoop
directory. After you run the query you need to (B) copy this directory
to the local directory of the AWS master node, then (C) copy this directory
from the AWS master node to your local machine.

#### 1.A. Create the "/user/hadoop Directory" in the Hadoop Filesystem

You will need to do this for each new job flow that you create.

To create a `/user/hadoop` directory on the AWS cluster's HDFS
file system run this from the AWS master node:
    
    % hadoop dfs -mkdir /user/hadoop
    

Check that the directory was created by listing it with this command:

    % hadoop dfs -ls /user/hadoop
    

You may see some output from either command, but you should not see any
errors.

You can also do this directly from grunt with the following command.

    grunt> fs -mkdir /user/hadoop 

Now you are ready to run your first sample program. Take a look at the
starter code that we provided in the course materials repo. Copy and paste
the content of `example.pig.`

**Note**: The program may appear to hang with a 0% completion
time... go check the job tracker. Scroll down. You should see a MapReduce
job running with some non-zero progress.

**Note 2**: Once the first MapReduce job gets to 100%...
if your grunt terminal still appears to be suspended... go back to the
job tracker and make sure that **the reduce phase is also 100% complete**.
It can take some time for the reducers to start making any progress.

**Note 3**: The example generates more than 1 MapReduce job...
so be patient.

#### 1.B. Copying files from the Hadoop Filesystem

The result of a pig script is stored in the hadoop directory specified
by the `store` command. That is, for `example.pig`,
the output will be stored at
`/user/hadoop/example-results`,
as specified in the script. HDFS is separate from the master node's file
system, so before you can copy this to your local machine, you must copy
the directory from HDFS to the master node's Linux file system:
    
    % hadoop dfs -copyToLocal /user/hadoop/example-results example-results

This will create a directory `example-results` with `part-*` files
in it, which you can copy to your local machine with `scp`. You
can then concatenate all the `part-*` files to get a single results
file, perhaps sorting the results if you like.

An easier option may be to use

    % hadoop fs -getmerge  /user/hadoop/example-results example-results

This command takes a source directory and a destination file as input
and concatenates files in src into the destination local file.

  
Use `hadoop dfs -help` or see the [`hadoop dfs` guide](http://hadoop.apache.org/docs/stable/file_system_shell.html)
to
learn how to manipulate HDFS. (Note that `hadoop fs` is the same
as `hadoop dfs`.)
  

#### 1.C. Copying files to or from the AWS master node
  * To copy one file from the master node back to your computer, run this
command _on the local computer:_
  
  

    $ scp -o "ServerAliveInterval 10" -i </path/to/saved/keypair/file.pem> hadoop@<master.public-dns-name.amazonaws.com>:<file_path> .
        

where `<file_path>` can be absolute or relative
to the AWS master node's home folder. The file should be copied onto your
current directory ('.') on your local computer.
  
  
  * Better: copy an entire directory, recursively. Suppose your files are
in the directory `example-results`. They type the following _on your loal computer_: 
    
    $ scp -o "ServerAliveInterval 10" -i </path/to/saved/keypair/file.pem> -r hadoop@<master.public-dns-name.amazonaws.com>:example-results .

  * As an alternative, you may run the scp command on the AWS master node,
and connect to your local machine. For that, you need to know your local
machine's domain name, or IP address, and your local machine needs to accept
ssh connections.

### 2\. Storing Files in S3

To use this approach, go to your AWS Management Console, click on Create
Bucket, and create a new bucket (=directory). Give it a name that may be
a public name. Do not use any special chatacters, including underscore.
Let's say you call it` superman`. Click on Actions, Properties,
Permissions. Make sure you have all the permissions.

Modify the store command of `example.pig` to:

     store count_by_object_ordered into 's3n://superman/example-results';

Run your pig program. When it terminates, then in your S3 console you
should see the new directory `example-results`. Click on individual
files to download. The number of files depends on the number of reduce
tasks, and may vary from one to a few dozens. The only disadvantage of
using S3 is that you have to click on each file separately to download.

Note that S3 is permanent storage, and you are charged for it. You can
safely store all your query answers for several weeks without exceeding
your credit; at some point in the future remember to delete them.

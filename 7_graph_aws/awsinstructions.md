## Setting up your AWS account 

Amazon will ask you for your credit card information during the
setup process. You will be charged for using their services.
You should not have to spend more than 10-20 dollars US.

Go to [http://aws.amazon.com/](http://aws.amazon.com/") and sign in or sign up.
You may sign in using your existing Amazon account, or, if you need an account:
1. Select "I am a new user".
2. Enter your contact information and confirm your acceptance of the AWS
Customer Agreement.
3. Once you have created an Amazon Web Services Account, you may need to
accept a telephone call to verify your identity. Some students have used
[Google Voice](https://www.google.com/voice) successfully if you don't have or don't want to give a
mobile number.
4. Return to [http://aws.amazon.com/](http://aws.amazon.com/) and sign in.

You'll be using three AWS services: Simple Storage Service (S3),
Elastic Compute Cloud (EC2), and Elastic MapReduce (EMR).

## Setting up an EC2 key pair

(Note AWS uses [several types of keys and credentials](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html),
for different purposes, including two types of keys: Access keys are used to
make remote API calls to AWS, or to use its command line tool from your own
machine. We won't need access keys for this quiz.)

To connect to an Amazon EC2 node, such as the master nodes for the Hadoop
clusters you will be creating, you need an SSH key pair. To create and
install one, do the following:

1. To create a key pair, follow the instructions at
[Amazon's instructions](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/generating-a-keypair.html),
in section "Having AWS create the key pair for you," subsection "AWS Management
Console." (Don't do this in Internet Explorer, or you might not be able
to download the .pem key file.)
2. Download and save the .pem key file to disk. In commands below, we will
refer to the .pem file as `</path/to/keypair.pem>`. (Replace this entire
string including the brackets with the location of your .pem file in the
following instructions.)
3. The local key setup differs for Linux / MacOS and Windows.
    * For Linux / MacOS: Make sure only you can access the .pem file.
    (If you do not change the permissions, you will get an error message later.)
    
        chmod 600 </path/to/keypair.pem>

    * For Windows, you can use
    [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) as your ssh
    client. PuTTy uses a different key file format from .pem, so you'll need
    to convert the key file into PuTTY format. Install PuTTy, then go to
    [http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)
    and follow the instructions in the section "Converting Your Private Key
    Using PuTTYgen".

## Starting an AWS Cluster and running Pig Interactively

To run a Pig job on AWS, you need to start up an AWS cluster using the
[Web Management Console](https://console.aws.amazon.com/elasticmapreduce/home)
and connect to the Hadoop master node.

Since you'll be charged for use of the cluster once it is created, you should
prepare the Pig code for at least the first part of the assignment before
starting your cluster. You can terminate the cluster in between parts of the
assignment, and set up a new one when you're ready for the next part.

### Creating the cluster

These instructions show use of the "quick setup".  There is also an "advanced"
setup option that may be needed if your job runs out of memory and you need to
set memory options.

1. Go to
[http://console.aws.amazon.com/elasticmapreduce/home](http://console.aws.amazon.com/elasticmapreduce/home)
and sign in.
2. Click "Create Cluster".
3. Under General Configuration:
    * In the "Cluster Name" field, you can enter a name to identify the purpose
      of the cluster.
    * For Launch mode, Cluster should be selected (this is the default).
4. Under Software Configuration:
    * Select "Core Hadoop".
5. Under Hardware Configuration:
    * Select the instance type. For most parts of this quiz, c1.medium will be
      fine. For the last quiz question, a larger instance size like m2.xlarge
      or m3.xlarge may be appropriate.
    * For number of instances, select 1 for now. For the last quiz question,
      you can select up to 20.
6. Security and access:
    * Select the name of the key pair you created earlier.
7. When you're ready, click Create cluster.
8. This will open the Cluster Details page. You can see the requested instances
being acquired and provisioned toward the right side of the form. The state of
the cluster overall is shown near the top of the page.
9. Now you need to obtain the Master Public DNS Name. After the cluster has
started this will be shown near the top of the Cluster Details page. In the
following instructions, we call this Master Public DNS name `<master DNS>`.
  
Now you are ready to connect to your cluster and run Pig jobs.

### Connecting to the master node from Linux or MacOS

From a terminal, use the following command (replace `</path/to/keypair.pem>`
and `<master DNS>` with your values):

    ssh -o "ServerAliveInterval 10" -i </path/to/keypair.pem> hadoop@<master DNS>

### Connecting to the master node from Windows

1. Start Pageant (the PuTTy key manager).
2. Find the Pageant icon in your System Tray, right-click, select Add Key.
3. Select the .ppk file you created earlier, Open, enter your pass-phrase.
4. Start PuTTy.
5. In the Host Name field, enter `hadoop@<master DNS>`
   (substituting the Master Public DNS name for your cluster).
6. In the Port field, enter 22.
7. For Connection type, select SSH.
8. Click Open.

### Starting the pig shell
  
Once you connect successfully, just type 
    
    pig

Now you should have a Pig prompt:

    grunt>
    
In this quiz we will use pig only interactively. (The alternative
is to have pig read the program from a file.)
  
This is the interactive mode where you type in pig queries. Here you will
cut and paste `example.pig`. You are now ready to return to the
quiz.

Other useful information:
* Hadoop will create the output directory for
you automatically. But Hadoop refuses to overwrite existing results. So
you will need to move your prior results to a different directory before
re-running your script, specify a different output directory in the script,
or delete the prior results altogether.
* To exit pig, type `quit` at the `grunt>` prompt. To
terminate the ssh session, type `exit` at the Linux shell prompt. After
that you must terminate the AWS cluster
(see ["Terminating an AWS cluster"](#terminating-an-aws-cluster)).
* To kill a pig job type CTRL/C while pig is running.This kills pig only:
after that you need to kill the hadoop job. We show you how to do this
below.
* After a hadoop job completes, you will need to exit from pig and re-start
it before you can run another job.
* To see how to perform these tasks and more, see
["Managing the results of your Pig queries"](#managing-the-results-of-your-pig-queries)
below.

## Monitoring Hadoop jobs

The master node provides web pages for monitoring Hadoop jobs and HDFS use,
but they are only accessible locally on the master. You can view them using
a text browser while connected to the master via ssh, but to view them from
your local browser, you'll either need to set up an SSH tunnel or SOCKS proxy.
An SSH tunnel is likely the easiest option.

The web pages are provided on two local ports on the master:
* Hadoop monitor: 8088
* HDFS monitor: 50070

### Easy Way: SSH Tunneling

Note you'll need two free local ports to use for the local end of the
SSH tunnel. Ports 8081 and 8082 are often free and not blocked by the firewall.
These are used in the examples.  If these aren't available, instructions are
shown for checking which ports are in use.

#### SSH Tunneling from Linux or MacOS

1. Check that ports 8081 and 8082 are open, or find two free local ports:
    * On Linux, open a terminal and type `netstat -antu` to see which ports are
    in use.
    * On MacOS, follow the instructions
    [here](https://support.apple.com/kb/PH18539).
2. Run this command (substitute your free local ports if they are not 8081
and 8082).
        ssh -L 8081:localhost:8088 -L 8082:localhost:50070  -i </path/to/keypair.pem> hadoop@<master DNS>
3. Open your browser to:
    * Hadoop monitor: [http://localhost:8081](http://localhost:8081)
    * HDFS monitor: [http://localhost:8082](http://localhost:8082)
  
From there, you can monitor your jobs' progress using the UI.

#### SSH Tunneling from Windows using PuTTy

(This assumes you have started Pageant and added your keys, as shown in
"Connecting to the master node from Windows".)

1. Check that ports 8081 and 8082 are open, or find two free local ports:
    * Open a command prompt window.
    * Enter: `netstat -an`
    * The ports shown in the Local Address column are in use -- if 8081 or 8082
    are in use pick something that is not in use.
1. Start PuTTy.
1. Go to Connection -> SSH -> Tunnels
1. In the "Add new forwarded port" section, fill in:
    * Source port: 8081 (or the free port you found)
    * Destination: `<master DNS>:8088` (recall this is the Master Public DNS
    for your cluster)
    * Check that Local and Auto are selected.
    * Click Add.
1. Now go to Session.
1. In the Host Name field, enter `hadoop@<master DNS>`
1. In the Port field, enter 22.
1. For Connection type, select SSH.
1. Click Open.
1. Accept the host key (if you haven't already done so).
1. You can minimize the window.
1. Repeat steps above starting with "Start PuTTy", except change the source and
destination ports:
    * Source port: 8082
    * Destination: `<master DNS>:50070`
1. Open these URLs in your browser:
    * Hadoop monitor: [http://localhost:8081](http://localhost:8081)
    * HDFS monitor: [http://localhost:8082](http://localhost:8082)

### Text browser: Lynx

[Lynx](http://lynx.isc.org/) is a text browser -- it shows only the text from
web pages -- in a terminal. This option is very easy. Open a separate `ssh`
connection to the AWS master node and type:
  
    lynx http://localhost:8088/
  
Navigate as follows:
* up/down arrows = move through the links (current link is highlighted)
* enter = follows a link
* left arrow = return to previous page

Examine the webpage carefully, while your pig program is running. You
should find information about the map tasks, the reduce tasks, you should
be able to drill down into each map task (for example to monitor its progress);
you should be able to look at the log files of the map tasks (if there
are runtime errors, you will see them only in these log files).
  
### SOCKS Proxy

Using SOCKS proxy, and your own browser. (This shows using local port 8888.
See the SSH Tunneling sections for how to check for unused local ports,
and substitute a different port if 8888 is in use.)

1. Set up your browser to use a proxy when connecting to the master node.
   (Note: Instructions are for Firefox and Chrome. If the instructions fail for
   one browser, try the other browser.
In particular, it seems like people are having problems with Chrome but
Firefox, especially following Amazon's instructions, works well.)
    * Firefox:
        1. Install the [FoxyProxy extension](https://addons.mozilla.org/en-US/firefox/addon/2464/) for Firefox.
        2. Copy the `foxyproxy.xml` configuration file from the course materials
repo into your [Firefox profile folder](http://support.mozilla.com/kb/profiles).
        3. If the previous step doesn't work for you, try deleting the `foxyproxy.xml` you
copied into your profile, and using
[Amazon's instructions](http://docs.amazonwebservices.com/ElasticMapReduce/latest/DeveloperGuide/UsingtheHadoopUserInterface.html#AccessingtheHadoopUserInterfacetoMonitorJobStatus2) to set up FoxyProxy manually.
If you use Amazon's instructions, be careful to use port 8888 instead of
the port in the instructions.
    * Chrome:
        * Option 1: FoxyProxy is [now available for Chrome](http://getfoxyproxy.org/downloads.html) as
well.
        * Option 2: You can try [proxy switch!](https://chrome.google.com/webstore/detail/caehdcpeofiiigpdhbabniblemipncjj)
            1. Click the _Tools_ icon (upper right corner; don't confuse it with
the Developer's Tools !), Go to _Tools_, go to _Extensions_.
Here you will see the ProxySwitch!: click on _Options_.
            2. Create a new Proxy Profile: Manual Configuration, Profile name = Amazon
Elastic MapReduce (any name you want), SOCKS Host = localhost, Port = 8888,
SOCKS v5\. If you don't see "SOCKS", de-select the option to "Use the same
proxy server for all protocols".
            3. Create two new switch rules (give them any names, say AWS1 and AWS2).
                * Rule 1: pattern=\*.amazonaws.com:\*/\*
                * Rule 2: pattern=\*.ec2.internal:\*/\*

            For both, Type=wildcard, Proxy profile=\[the profile you created at the
previous step\].

2. Open a new local terminal window and create the SSH SOCKS tunnel to the
master node using the following: 
    
        ssh -o "ServerAliveInterval 10" -i </path/to/keypair.pem> -ND 8888 hadoop@<master DNS>

    (The `-N` option
tells `ssh` not to start a shell, and the `-D 8888` option
tells `ssh` to start the proxy and have it listen on port 8888.)

    The resulting SSH window will appear to hang, without any output; this
is normal as SSH has not started a shell on the master node, but just created
the tunnel over which proxied traffic will run.

    Keep this window running in the background (minimize it) until you are
finished with the proxy, then close the window to shut the proxy down.
3. Open these URLs in your browser:
    * Hadoop monitor: `http://<master DNS>:8088/`
    * HDFS monitor: `http://<master DNS>:50070/`

## Killing a Hadoop Job

Later, in the assignment, we will show you how to launch MapReduce jobs
through Pig. You will basically write Pig Latin scripts that will be translated
into MapReduce jobs (see lecture notes). Some of these jobs can take a
long time to run. If you decide that you need to interrupt a job before
it completes, here is the way to do it:

If you want to kill pig, you first type CTRL/C, which kills pig only.
Next, kill the hadoop job, as follows. From the Hadoop monitor find
the hadoop `job_id`, then type:

`hadoop job -kill job_id`

Note this is not the normal way to exit from pig. If your MapReduce completes
successfully, all the hadoop jobs will exit.

## Terminating an AWS cluster

When you are done running Pig scripts, make sure to **ALSO** terminate
your cluster. This is a step that you need to do **in addition to **stopping
pig and Hadoop (if necessary) above.

This step shuts down your AWS cluster:
1. Go to the [EMR Management Console](https://console.aws.amazon.com/elasticmapreduce/home)
2. Select the job in the list.
3. Click the Terminate button.  (If termination protection is on, you will be
prompted to turn it off before you can terminate the cluster.)
4. Wait for a while (may take minutes) and recheck until the job state becomes
TERMINATED. You may need to refresh the cluster details page.

**Pay attention to this step**. If you fail to terminate
your job and only close the browser, or log off AWS, your cluster will continue
to run, and AWS will continue to charge you: for hours, days, weeks, and
it charges this to your credit card automatically. Make sure you
don't leave the console until you have confirmation that the cluster is terminated.

Since this step releases the master node, any connections to it will end.
So you can close any ssh connections.

## Checking your Balance 

Please check your balance regularly!!!
1. Go to the [EMR Management Console](https://console.aws.amazon.com/elasticmapreduce/home)
2. Click on your name in the top right corner and select "Account Activity".
3. Now click on "detail" to see any charges < $1\.

To avoid unnecessary charges, terminate your cluster when you are not
using it.

**USEFUL**: AWS customers can now use **billing alerts** to
help monitor the charges on their AWS bill. You can get started today by
visiting your [Account Activity page](https://aws-portal.amazon.com/gp/aws/developer/account/index.html) to enable monitoring of your charges.
Then, you can set up a billing alert by simply specifying a bill threshold
and an e-mail address to be notified as soon as your estimated charges
reach the threshold. 

## Managing the results of your Pig queries

Your pig program stores the results in several files in a directory -- there
will be one file for each reducer. You
have two options:
* (1) Store these files in the Hadoop File System (HDFS).
If you use HDFS, the files will be discarded when your cluster is shut down.
* (2) Store these files in S3\.
If you use S3, the files will persist (and you'll be charged for storage)
until you delete them.

### (1) Storing Files in the Hadoop File System

This is done through the following pig command (used in `example.pig`):

    store count_by_object_ordered into '/user/hadoop/example-results' using PigStorage();

Pig will not run any commands until it has to, so it will not start the
MapReduce job until you run the `store` command.

After the MapReduce job completes, you will need to copy this directory
to the local directory of the AWS master node, then, if you want, copy this
from the AWS master node to your local machine.

#### Check that the /user/hadoop directory is present

Hadoop reducers write their output to HDFS. In the new release of EMR, an
HDFS directory called `/user/hadoop` should be created automatically.
Check that the directory exists by listing it with this command:

    hadoop fs -ls /user/hadoop

If there is an error, create a `/user/hadoop` directory with this command:
    
    hadoop fs -mkdir /user/hadoop

You can also do this directly from grunt with the following command.

    fs -mkdir /user/hadoop 

#### Copying files from the Hadoop Filesystem

The result of a pig script is stored in the hadoop directory specified
by the `store` command. That is, for `example.pig`,
the output will be stored at
`/user/hadoop/example-results`,
as specified in the script. HDFS is separate from the master node's file
system, so before you can copy this to your local machine, you must copy
the directory from HDFS to the master node's Linux file system:
    
    hadoop fs -copyToLocal /user/hadoop/example-results example-results

This will create a directory `example-results` with `part-*` files
in it, which you can copy to your local machine with `scp`. You
can then concatenate all the `part-*` files to get a single results
file, perhaps sorting the results if you like.

An easier option may be to use

    hadoop fs -getmerge  /user/hadoop/example-results example-results

This command takes a source directory and a destination file as input
and concatenates files in src into the destination local file.

Use `hadoop fs -help` or see the
[`hadoop fs` guide](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html)
to learn how to manipulate HDFS.

#### Copying files to or from the AWS master node, using Linux or MacOS

To copy one file from the master node back to your computer, run this
command _on the local computer:_

    scp -o "ServerAliveInterval 10" -i </path/to/keypair.pem> hadoop@<master DNS>:<file_path> .

where `<file_path>` can be absolute or relative
to the AWS master node's home folder. The file should be copied onto your
current directory ('.') on your local computer.
  
Better: copy an entire directory, recursively. Suppose your files are
in the directory `example-results`. They type the following _on your loal computer_: 
    
    scp -o "ServerAliveInterval 10" -i </path/to/keypair.pem> -r hadoop@<master DNS>:example-results .

As an alternative, you may run the scp command on the AWS master node,
and connect to your local machine. For that, you need to know your local
machine's domain name, or IP address, and your local machine needs to accept
ssh connections.

#### Copying files to or from the master node, using Windows

The simplest method is to use an application designed for this, such as
[WinSCP](http://winscp.net/). This works with PuTTy's Pageant, so it can use
your AWS EC2 ssh keys after you start Pageant.

### (2) Storing Files in S3

To use this approach, go to your AWS Management Console, click on Create
Bucket, and create a new bucket (= directory). Give it a name that may be
a public name. Do not use any special characters, including underscore.
Let's say you call it` superman`. Click on Actions, Properties,
Permissions. Make sure you have all the permissions.

Modify the store command of `example.pig` to:

    store count_by_object_ordered into 's3n://superman/example-results';

After your pig program completes, you should see, in your
[S3 console](https://console.aws.amazon.com/s3/home),
the new directory `example-results`. Click on individual
files to download. The number of files depends on the number of reduce
tasks, and may vary from one to a few dozens. The only disadvantage of
using S3 is that you have to click on each file separately to download.

Note that S3 is permanent storage, and you are charged for it.

## Run `example.pig`

Now you are ready to run your first sample program. Take a look at the
starter code that we provided in the course materials repo. Copy and paste
the content of `example.pig.`

Note:
* The program may appear to hang with a 0% completion
time. Go check the Hadoop monitor. You should see a task
running with some non-zero progress.
* Once the first task gets to 100%,
if your grunt terminal still appears to be suspended, go back to the
Hadoop monitor and make sure that *the reduce phase is also 100% complete*.
It can take some time for the reducers to start making any progress.
(There is also a progress bar on the cluster details web page.)
* The example generates more than 1 MapReduce job so be patient.

As described earlier, monitor your job as it runs.
When it's done, copy your results and *terminate your cluster*.
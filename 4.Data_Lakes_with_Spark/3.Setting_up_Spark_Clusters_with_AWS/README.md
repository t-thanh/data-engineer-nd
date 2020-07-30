# Setting up Spark Clusters with AWS
## [Introduction](https://youtu.be/efzIn_CtvAM)

### Lesson Overview
By the end of the lesson, you will be able to:

- Distinguish between setting up a Spark Cluster using both Local and Standalone Mode
- Set up Spark Cluster in AWS - Use Spark UI
- Use AWS CLI
- Create EMR using AWS CLI
- Create EMR Cluster
- Test Port Forwarding
- Use Notebooks on your Spark Cluster
- Write Spark Scripts
- Store and Retrieve data on the Cloud
- Read and Write to Amazon S3
- Understand the distinction between HDFS and S3
- Reading and Writing Data to HDFS

## [From Local to Standalone Mode](https://youtu.be/EeBWbABm_Qc)

### Overview of the Set up of a Spark Cluster

- **Amazon S3** will store the dataset.
- We rent a cluster of machines, i.e., our **Spark Cluster**, and iti s located in AWS data centers. We rent these using AWS service called **Elastic Compute Cloud (EC2)**.
- We log in from your local computer to this Spark cluster.
- Upon running our Spark code, the cluster will load the dataset from **Amazon S3** into the cluster’s memory distributed across each machine in the cluster.

#### New Terms:
- **Local mode**: You are running a Spark program on your laptop like a single machine.
- **Standalone mode**: You are defining Spark Primary and Secondary to work on your (virtual) machine. You can do this on EMR or your machine. Standalone mode uses a resource manager like YARN or Mesos.

## [Setup Instructions AWS](https://youtu.be/ZVdAEMGDFdo)
### EC2 vs EMR
|	        |AWS EMR	       |AWS EC2|
|----------:|:-------------|:------|
| **Distributed computing**	|Yes	|Yes|
| **Node categorization**	|Categorizes secondary nodes into core and task nodes as a result of which data can be lost in case a data node is removed.	|Does not use node categorization|
| **Can support HDFS?**	|Yes	|Only if you configure HDFS on EC2 yourself using multi-step process.|
| **What protocol can be used?**	|Uses S3 protocol over AWS S3, which is faster than s3a protocol	|ECS uses s3a |
| **Comparison cost**	|Bit higher	|Lower|

### Circling back about HDFS

Previously we have looked over the Hadoop Ecosystem. To refresh those concepts, we have provided reference material here. HDFS (Hadoop Distributed File System) is the file system. HDFS uses MapReduce system as a resource manager.

Spark can replace the MapReduce algorithm. Since Spark does not have its own distributed storage system, it leverages using HDFS or AWS S3, or any other distributed storage. Primarily in this course, we will be using AWS S3, but let’s review the advantages of using HDFS over AWS S3.

### What is HDFS?
HDFS (Hadoop Distributed File System) is the file system in the Hadoop ecosystem. Hadoop and Spark are two frameworks providing tools for carrying out big-data related tasks. While Spark is faster than Hadoop, Spark has one drawback. It lacks a distributed storage system. In other words, Spark lacks a system to organize, store and process data files.

### MapReduce System
HDFS uses MapReduce system as a resource manager to allow the distribution of the files across the hard drives within the cluster. Think of it as the MapReduce System storing the data back on the hard drives after completing all the tasks.

Spark, on the other hand, runs the operations and holds the data in the RAM memory rather than the hard drives used by HDFS. Since Spark lacks a file distribution system to organize, store and process data files, Spark tools are often installed on Hadoop because Spark can then use the Hadoop Distributed File System (HDFS).

#### Why do you need EMR Cluster?
Since a Spark cluster includes multiple machines, in order to use Spark code on each machine, we would need to download and install Spark and its dependencies. This is a manual process. Elastic Map Reduce is a service offered by AWS that negates the need for you, the user, to go through the manual process of installing Spark and its dependencies for each machine.

#### Setting up AWS
Please refer to the latest [AWS documentation to set up an EMR Cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs-launch-sample-cluster.html).

## Alternate ways to connect to AWS using CLI

![](https://video.udacity-data.com/topher/2020/May/5ec81111_dend-refresh-02-1/dend-refresh-02-1.png)

### Why use AWS CLI?
AWS CLI enables you to run commands that allow access to currently available AWS Services. We can also use AWS CLI to primarily create and check the status of our EMR instances. Mostly during your work, you would normally create clusters that are similar in sizes and functionalities, and it can get tedious when you use the AWS console to create a cluster. If you have a pre-generated script to generate EMR saved to your text editor, you can re-run as often as you’d like to generate new clusters. This way we can bypass setting security groups and roles through AWS console. You can embed all these features, including selecting number of cores, applications to install, and even custom script to execute at the time of cluster launch by using a pre-generated script.

### How to use AWS CLI?
- We’ll be using AWS CLI to create an EMR cluster.
- Check to see if you have Python 3.6 or above
- You can check the Python version using the command line: `$ python --version`
- Install AWS CLI using `pip install awscli`.
- Check if `AWS CLI` is installed correctly by typing `aws` into your terminal.
- If you see the image below, you have installed `AWS CLI` correctly.

![](https://video.udacity-data.com/topher/2020/April/5ea0f839_unnamed/unnamed.png)

### Setting up credentials using AWS IAM
Let’s set up **AWS IAM**. This is a service in AWS to create and manage your credentials for AWS services by creating a permission file and secret access key pairs.

The permission file and the secret access key pairs will be stored to your computer for accessing AWS services.

### How to navigate to the AWS IAM page
- From the AWS console, type IAM in the search bar.
- This will direct to the Identity and Access Management page.
- Click on the Dashboard from left.
- Click on Management Security Credentials.

![](https://video.udacity-data.com/topher/2020/April/5ea0f868_aws-iam-page/aws-iam-page.png)

This should take you to the following page.

![](https://video.udacity-data.com/topher/2020/April/5ea0f890_aws-iam-access-keys-dashboard/aws-iam-access-keys-dashboard.png)

### Storing Key Pairs

Once you’ve created the Key Pairs, make sure you **store the `Secret Key` into some secure place** because you will not be able to view this again. Let’s save this into your computer as well so that AWS CLI can access these keys.

Navigate to your home folder (simply type cd in your terminal)
Create a directory mkdir .aws
Make sure to have that period to denote a hidden directory.
Create a file called credentials in the directory.
Store the key pairs here as well as the default configuration for your AWS clusters.
![](https://video.udacity-data.com/topher/2020/April/5ea0f8ed_example-image-of-credentials-and-config/example-image-of-credentials-and-config.png)

## Create EMR Using AWS CLI

### Creating EMR Script
While creating EMR through AWS console has been shown, but if you know the specificity of your instances, such as which applications you need or what kind of clusters you’ll need, you can reuse the EMR script that we will create below multiple times.
```
aws emr create-cluster --name <cluster_name> \
 --use-default-roles --release-label emr-5.28.0  \
--instance-count 3 --applications Name=Spark Name=Zeppelin  \
--bootstrap-actions Path="s3://bootstrap.sh" \
--ec2-attributes KeyName=<your permission key name> \
--instance-type m5.xlarge --log-uri s3:///emrlogs/
```

### Learning Components on EMR Script
Let’s break down the code and go over each part of the code in the EMR script. It’s important that you know what each component does in order to launch a proper cluster and services attached to this script.

### EMR Script Components
- `aws emr` : Invokes the AWS CLI, and specifically the command for EMR.
- `create-cluster` : Creates a cluster
- `--name` : You can give any name for this - this will show up on your AWS EMR UI. This can be duplicate as existing EMR.
- `--release-label`: This is the version of EMR you’d like to use.
- `--instance-count`: Annotates instance count. One is for the primary, and the rest are for the secondary. For example, if --instance-count is given 4, then 1 instance will be reserved for primary, then 3 will be reserved for secondary instances.
- `--applications`: List of applications you want to pre-install on your EMR at the launch time
- `--bootstrap-actions`: You can have a script stored in S3 that pre-installs or sets
environmental variables, and call that script at the time EMR launches
- `--ec2-attributes` `KeyName`: Specify your permission key name, for example, if it is MyKey.pem, just specify MyKey for this field
- `--instance-type`: Specify the type of instances you want to use. Detailed list can be accessed here, but find the one that can fit your data and your budget.
- `--log-uri`: S3 location to store your EMR logs in. This log can store EMR metrics and also the metrics/logs for submission of your code.

Now it’s your turn to create your own EMR script.

### Exercise: Create Your Own EMR Script

**NOTE 1: Do not forget to add the `--auto-terminate` field because EMR clusters are costly. Once you run this script, you’ll be given a unique cluster ID.**

**NOTE 2. Check the status of your cluster using `aws emr --cluster-id <cluster_id>`.**

For this exercise, we will be creating an EMR cluster.

- *Step 1*. Install `awscli` using `pip`.

    - You can get instructions for MacOS, Windows, Linux here on [AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

- *Step 2*. This will give you **access to create an EMR cluster and EC2 cluster**.

    - The EC2 cluster shows a status of all the clusters with your keys, etc.

- *Step 3*. Once it's installed, run the script below to launch your cluster.

    - Be sure to include the appropriate file names within the <> in the code.

```python
# Add your cluster name
aws emr create-cluster --name <YOUR_CLUSTER_NAME> 
--use-default-roles  
--release-label emr-5.28.0
--instance-count 2 
--applications Name=Spark  
--bootstrap-actions Path=<YOUR_BOOTSTRAP_FILENAME> 
--ec2-attributes KeyName=<YOUR_KEY_NAME>
--instance-type m5.xlarge 
--instance-count 3 --auto-terminate`

# Specify your cluster name 
`YOUR_CLUSTER_NAME: <INPUT NAME HERE>

# Insert your IAM KEYNAME - 
# Remember, your IAM key name is saved under .ssh/ directory
YOUR_KEY_NAME: <IAM KEYNAME>

# Specify your bootstrap file. Please note that this step is optional. 
# It should be an executable (.sh file) in an accessible S3 location. 
# If you aren't going to use the bootstrap file, 
# you can remove the `--bootstrap-actions` tag above.
# This file is provided in the zipped folder titled
# “Exercise_Creating EMR Cluster” at the bottom of this page.

# In this EMR script, execute using Bootstrap
YOUR_BOOTSTRAP_FILENAME: <BOOTSTRAP FILE> 
```
A copy of the exercises are also available in the lesson git repo: Here is the [Link to Github](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Setting_Spark_Cluster_In_AWS/exercises/starter)

### Desired Output
#### The output should look like this:
```
{
    "ClusterId": "j-2PZ79NHXO7YYX",
    "ClusterArn": "arn:aws:elasticmapreduce:us-east-2:027631528606:cluster/j-2PZ79NHXO7YYX"
}


# Go to AWS EMR console from your web browser, 
# then check if the cluster is showing up.

#Or you can type

aws emr describe-cluster --cluster-id <CLUSTER_ID FROM ABOVE>`

# You can run `aws emr describe-cluster --cluster-id j-2PZ79NHXO7YYX`
# to confirm if this cluster is ready to go.
```

### Changing Security Groups

1. Once you launch your instance, we will want to log in. Alternately you can use SSH protocol (allows secure remote login) to access your master node on the EMR cluster. Each cluster gets its own security setting.
2. You’ll need to allow EMR to accept incoming SSH protocol so your local machine can connect to your EMR cluster in the AWS Cloud by changing the security group.
3. Next, we’ll be making the SSH connection from your laptop to your EMR cluster. To allow this, we’ll need to change the Security Group on EC2.

Let’s log into AWS EC2 console.

~[](https://video.udacity-data.com/topher/2020/April/5ea0fe77_changing-security-group-on-ec2-console/changing-security-group-on-ec2-console.png)

### Setting up Port Forwarding

1. One last thing to do before using the Jupyter Notebook, or even browsing the Spark UI, is to set up proxy.
2. Let’s install FoxyProxy on your Chrome or Firefox browser.

Here is the link to [Amazon’s documentation on managing clusters using it’s web interfaces](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html)

### Testing Port Forwarding

Let’s see if your port forwarding works!

```
# SSH into your cluster first. Note that the port number matches 
# what is in foxyproxy-settings.xml.
ssh -i ~/.aws/<YOUR_PEM_FILE>.pem hadoop@<YOUR IP> -ND 8157

# Open another terminal tab, then copy this code into your cluster 
# with your PEM file .
scp -i ~/.aws/<YOUR_PEM_FILE>.pem hadoop@<YOUR IP>:/home/hadoop/

# Execute the file
python spark_test_script.py

# Open up Resource Manager Tab from AWS console
# If you’re able to see the Resource Manager from your browser,
#  then you have successfully done port forwarding.
```

Click on the Spark UI from the cluster management site. If this is directed to another tab and shows you the Spark executor information, you have done port forwarding successfully!

You should be able to see those application names turn into blue - as in clickable link, then you can tell your port forwarding has been successful.

### See below for the desired screen.
![](https://video.udacity-data.com/topher/2020/April/5ea0ff3b_resource-manager-dashboard/resource-manager-dashboard.png)

Supporting Materials
 [Exercise Create EMR Clusters](https://video.udacity-data.com/topher/2020/April/5ea2af82_exercise-create-emr-clusters/exercise-create-emr-clusters.zip)

## [Using Notebooks on Your Cluster](https://youtu.be/EcIYPkCkehY)

### Jupyter / Zeppelin Notebook
There are a couple of options for which notebook to use. We can use a Jupyter Notebook, or use a Zeppelin notebook. If you are already familiar with Jupyter Notebooks, continue using them.

#### Advantages of using Zeppelin Notebook

While the use of Jupyter Notebook is common across the industry, you can explore using Zeppelin notebooks. Zeppelin notebooks have been available since EMR 5.x versions, and they have direct access to Spark Context, such as a local spark-shell. For example, if you type `sc`, you’ll be able to get Spark Context within Zeppelin notebooks.

Zeppelin is very similar to Jupyter Notebook, but if you want to use other languages like Scala or SQL, on top of using Python, you can use Zeppelin instead.

## [Spark Scripts](https://youtu.be/bfOocPv54EI)

## [Submitting Spark Scripts](https://youtu.be/ZcSfIqAgoUQ)

### Submitting Spark Script Instructions

Here is the link to the [GitHub repo](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Setting_Spark_Cluster_In_AWS/exercises/starter) where a copy of the exercise instructions are located along with cities.csv file.

- Download the cities.csv dataset to your local machine.
- Upload a file into an S3 location using the AWS S3 console, or you can use the AWS CLI command, like 

```
aws s3 cp <your current file location>/<filename> s3://<bucket_name>
```

- Create an EMR instance.
- Copy the file to your EMR instance, preferably in your home directory of EMR instance.
- Execute the file using `spark-submit <filename>.py`.

#### A note about SSH

SSH is a specific protocol for secure remote login and file transfer.

The instructor is showing you one way to save your files. He is using SSH protocol to save the files in the EMR instance. When you see `hadoop@ip-###- ###-####`, this indicates that the instructor accessed the EMR instance using SSH protocol. However, once he terminates the EMR instance, everything he would saved on the EMR instance will be lost. This is because EMR instance is not kept active all the time since it is expensive.

In the *Reflection Exercise* you can experiment with an alternate good industry practice. Data engineers always save their initial, final, and intermediate data of the data pipeline in the S3 for future retrieval. It is best practice to move your files from your local machine to AWS S3, then use the program to read the data from AWS S3.

### Reflection exercise:
Use your proxy to view the Spark UI to understand how your code and workers are working, i.e. which are transformation vs action words (and if they are correctly showing up on Spark UI), and to get familiar with reading the Spark UI. This will give you a better understanding on how your Spark program runs.

**Reminder link** to [Amazon documentation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html) on FoxyProxy

Supporting Materials
 [Cities](https://video.udacity-data.com/topher/2020/May/5eabf02f_cities/cities.csv)

## [Storing and Retrieving Data on the Cloud](https://youtu.be/MrF2sHdpXJo)

## Reading and Writing to Amazon S3

### S3 Buckets

With the convenient AWS UI, we can easily mistake AWS S3 (Simple Storage Service) equivalent as Dropbox or even Google Drive. This is not the case for S3. S3 stores an object, and when you identify an object, you need to specify a bucket, and key to identify the object. For example,
```
df = spark.read.load(“s3://my_bucket/path/to/file/file.csv”)
```
From this code, `s3://my_bucket` is the bucket, and `path/to/file/file.csv` is the key for the object. Thankfully, if we’re using spark, and all the objects underneath the bucket have the same schema, you can do something like below.
```
df = spark.read.load(“s3://my_bucket/”)
```

This will generate a dataframe of all the objects underneath the `my_bucket` with the same schema. Pretend some structure in s3 like below:
```
my_bucket
  |---test.csv
  path/to/
     |--test2.csv
     file/
       |--test3.csv
       |--file.csv
```

If all the csv files underneath `my_bucket`, which are `test.csv`, `test2.csv`, `test3.csv`, and `file.csv` have the same schema, the dataframe will be generated without error, but if there are conflicts in schema between files, then the dataframe will not be generated. As an engineer, you need to be careful on how you organize your data lake.

### [Video 1](https://youtu.be/j4kpT3DQ8i8)

### [Video 2](https://youtu.be/yXfb4vwg7aM)

[Link to Github Repo](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Setting_Spark_Cluster_In_AWS/demo_code) on Demo code referred to in video: [HERE](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Setting_Spark_Cluster_In_AWS/demo_code)

Supporting Materials
 [Reading And Writing To AmazonS3](https://video.udacity-data.com/topher/2020/May/5ebba92c_reading-and-writing-to-amazons3/reading-and-writing-to-amazons3.zip)

## [Understanding difference between HDFS and AWS S3](https://youtu.be/vsB_VLoiwyc)

### Differences between HDFS and AWS S3

Since Spark does not have its own distributed storage system, it leverages using HDFS or AWS S3, or any other distributed storage. Primarily in this course, we will be using AWS S3, but let’s review the advantages of using HDFS over AWS S3.

Although it would make the most sense to use AWS S3 while using other AWS services, it’s important to note the differences between AWS S3 and HDFS.

- **AWS S3** is an **object storage system** that stores the data using key value pairs, namely bucket and key, and **HDFS** is an **actual distributed file system** which guarantees fault tolerance. HDFS achieves fault tolerance by having duplicate factors, which means it will duplicate the same files at 3 different nodes across the cluster by default (it can be configured to different numbers of duplication).

- HDFS has usually been **installed in on-premise systems**, and traditionally have had engineers on-site to maintain and troubleshoot Hadoop Ecosystem,** which cost more than having data on cloud**. Due to the **flexibility of location** and **reduced cost of maintenance**, cloud solutions have been more popular. With extensive services you can use within AWS, S3 has been a more popular choice than HDFS.

- Since **AWS S3 is a binary object store**, it can **store all kinds of format**, even images and videos. HDFS will strictly require a certain file format - the popular choices are **avro** and **parquet**, which have relatively high compression rate and which makes it useful to store large dataset.

## [Reading and Writing Data to HDFS](https://youtu.be/IVdbgtCLnmA)

## [Recap Local Mode to Cluster Mode](https://youtu.be/W434NZOxrhk)
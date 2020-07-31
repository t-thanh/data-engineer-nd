# Introduction to Data Lakes
## [Introduction](https://youtu.be/kv08_VWQ2Ho)
## [Lesson Overview](https://youtu.be/fLzYJsJozvM)
## [Why Data Lakes: Evolution of the Data Warehouse](https://youtu.be/3KSt8-nFUo0)
## [Why Data Lakes: Unstructured & Big Data](https://youtu.be/niF5i3qsagM)
## [Why Data Lakes: New Roles & Advanced Analytics](https://youtu.be/3B7iv1GRaAw)
## [Big Data Effects: Low Costs, ETL Offloading](https://youtu.be/-snvU7S3wZo)
## [Big Data Effects: Schema-on-Read](https://youtu.be/cBvKpHfTLTA)
## [Big Data Effects: (Un-/Semi-)Structured support](https://youtu.be/5R8y9Xa8izs)
## [Demo: Schema On Read Pt 1](https://youtu.be/_clMPKkFytg)
## [Demo: Schema On Read Pt 2](https://youtu.be/_GUDMCEaX0Y)
## [Demo: Schema On Read Pt 3](https://youtu.be/EN0AJPNjyeE)
## [Demo: Schema On Read Pt 4](https://youtu.be/m1kD8EyFPH0)
## [Demo: Advanced Analytics NLP Pt 1](https://youtu.be/_ZMWq5cZjzI)
## [Demo: Advanced Analytics NLP Pt 2](https://youtu.be/gx3JYVDitiE)
## [Demo: Advanced Analytics NLP Pt 3](https://youtu.be/Ymgj8KetT14)
## [Data Lake Implementation Introduction](https://youtu.be/wi0OXQpr81U)
## [Data Lake Concepts](https://youtu.be/DozXTpjZjas)
## [Data Lake vs Data Warehouse](https://youtu.be/2YkwP4jw8ig)
## AWS Setup

### AWS Account and Credits

If you are working your way through the Data Engineering Nanodegree, you have prob**ably already set up an AWS account and received your promotional credits earlier in the program. If not, before you complete the exercises and project in this Data Lakes course, you will need to go to the lesson "Introduction to the Cloud and AWS" in the Data Warehouses course and follow the directions there to get yourself set up with AWS.**

Once you have your AWS account and credits set up, then continue on to the rest of the concepts in this lesson, and then to the project.

## [Data Lake Options on AWS](https://youtu.be/AMdFTlYWmp8)
## [AWS Options: EMR (HDFS + Spark)](https://youtu.be/m88kdMKB4qs)
## [AWS Options: EMR: S3 + Spark](https://youtu.be/ur1clGbA0Rw)
## [AWS Options: Athena](https://youtu.be/XNEczLKSISw)
## [Demo: Data Lake on S3 Pt 1](https://youtu.be/phZ2irpPtMM)
## [Demo: Data Lake on S3 Pt 2](https://youtu.be/kqy6w6kat58)
## [Demo: Data Lake on EMR Pt 1](https://youtu.be/539RnL05fGQ)
## [Demo: Data Lake on EMR Pt 2](https://youtu.be/lr-6oUkzs2w)
## [Demo: Data Lake on Athena Pt 1](https://youtu.be/Cy-kJEc5oKE)
## [Demo: Data Lake on Athena Pt 2](https://youtu.be/LWOTnS2wS9U)
## [Data Lake Issues](https://youtu.be/FCXdgt-IkTE)
## AWS - Launch EMR Cluster and Notebook

### Launch EMR Cluster and Notebook

Follow the instructions below to launch your EMR cluster and notebook.

- Open a regular AWS account (if you don't already have one) following the instructions via the [Amazon Web Service Help Center](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
- Go to the [Amazon EMR Console](https://console.aws.amazon.com/elasticmapreduce/)
- Select "Clusters" in the menu on the left, and click the "Create cluster" button.

### Step 1: Configure your cluster with the following settings:
- Release: `emr-5.20.0` or later
Applications: `Spark`: Spark 2.4.0 on Hadoop 2.8.5 YARN with Ganglia 3.7.2 and Zeppelin 0.8.0
Instance type: `m3.xlarge`
Number of instance: `3`
EC2 key pair: `Proceed without an EC2 key pair` or feel free to use one if you'd like

You can keep the remaining default setting and click "Create cluster" on the bottom right.

![](https://video.udacity-data.com/topher/2018/December/5c1a2f1a_configure-cluster/configure-cluster.png)

### Step 2: Wait for Cluster "Waiting" Status

Once you create the cluster, you'll see a status next to your cluster name that says *Starting*. Wait a short time for this status to change to *Waiting* before moving on to the next step.

![](https://video.udacity-data.com/topher/2018/December/5c1a25e5_cluster-waiting/cluster-waiting.png)

### Step 3: Create Notebook

Now that you launched your cluster successfully, let's create a notebook to run Spark on that cluster.

Select `Notebooks` in the menu on the left, and click the "Create notebook" button.

![](https://video.udacity-data.com/topher/2018/December/5c1a265e_create-notebook-button/create-notebook-button.png)

### Step 4: Configure your notebook

- Enter a name for your notebook
- Select "Choose an existing cluster" and choose the cluster you just created
- Use the default setting for "AWS service role" - this should be "EMR_Notebooks_DefaultRole" or "Create default role" if you haven't done this before.

You can keep the remaining default settings and click "Create notebook" on the bottom right.

![](https://video.udacity-data.com/topher/2018/December/5c1a26f1_configure-notebook/configure-notebook.png)

### Step 5: Wait for Notebook "Ready" Status, Then Open

Once you create an EMR notebook, you'll need to wait a short time before the notebook status changes from `Starting` or `Pending to Ready`. Once your notebook status is `Ready`, click the "Open" button to open the notebook.

![](https://video.udacity-data.com/topher/2018/December/5c1a28e2_notebook-ready/notebook-ready.png)

### Start Coding!

Now you can run Spark code for your project in this notebook, which EMR will run on your cluster. In the next page, you'll find starter code to create a spark session and read in the full 12GB dataset for the DSND Capstone project.

![](https://video.udacity-data.com/topher/2018/December/5c1a30d3_empty-notebook/empty-notebook.png)

### Download Notebook

When you are finished with your notebook, click `File` > `Download as` > `Notebook` to download it to your computer. On your local computer, create a git repository including this notebook and a README file. Submit the URL to your github repository to submit this project. See more details in the [Sparkify Project Overview page](https://classroom.udacity.com/nanodegrees/nd025/parts/84260e1f-2926-4127-895f-cc4432b05059/modules/80c955ce-72f2-403a-9bf5-cc58636dab9d/lessons/d6285247-6bc0-4783-b118-6f41981b9469/concepts/47d96c80-82da-4640-9fff-54415f2a21df).

![](https://video.udacity-data.com/topher/2018/December/5c1a3858_download-notebook/download-notebook.png)


For more information on EMR notebooks, click [here](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html).

### Pricing - Be Careful!

From this point on, AWS will charge you for running your EMR cluster. See details on this and how to manage your resources to avoid unexpected costs in the "Managing Resources" section at the end of this lesson.

## AWS - Avoid Paying Unexpected Costs

### Pricing - Be Careful!
From this point on, AWS will charge you for running your EMR cluster. You can find the details on the [EMR Pricing here](https://aws.amazon.com/emr/pricing/). If you run your cluster for a week with the settings specified earlier (3 instances of `m3.xlarge`), you should expect costs to be around $30, which should be covered in the amount of free promotional credits you have received from AWS as a Udacity student.

Most importantly, remember to terminate your cluster when you are done. Otherwise, your cluster might run for a day, week, month, or longer without you remembering, and you’ll wind up with a large bill!

### Terminate Your Cluster
You can terminate your cluster while still keeping the Jupyter notebook you created. In EMR, your EMR cluster and EMR notebook are decoupled (so you can reattach your notebook to a different cluster at any time)! To terminate your cluster, click "Clusters" in the menu on the left, check the box next to your cluster to select, and click the "Terminate" button.

![](https://video.udacity-data.com/topher/2018/December/5c1a1f63_terminate-cluster/terminate-cluster.png)

### Change Cluster for Notebook
If you still have a notebook on EMR and terminated the cluster it was connected to, you can still run that notebook at any time by creating another cluster (following the instructions in the previous section). Once you have the new cluster launched and in "waiting" status, click "Notebooks" in the menu on the left and click on the name of your notebook. Then click the "Change cluster" button.

![](https://video.udacity-data.com/topher/2018/December/5c1a3015_change-cluster-button/change-cluster-button.png)

Select your new cluster. Once your notebook reaches "Ready" status, you can now run this notebook on your new cluster.

![](https://video.udacity-data.com/topher/2018/December/5c1a305f_change-cluster/change-cluster.png)

### Delete Your Notebook
When you've finished with your project and downloaded your notebook, you can delete your notebook from EMR by selecting "Notebooks" in the menu on the left, selecting your notebook, and then clicking "Delete." Make sure to terminate the clusters you launched for this as well.

![](https://video.udacity-data.com/topher/2018/December/5c1a29ae_delete-notebook/delete-notebook.png)

### Delete S3 buckets
AWS charges primarily for running instances, so most of the charges will cease once you stop the cluster. However, there are smaller storage charges that continue to accrue if you don't delete your buckets. To delete your buckets, go to the [Amazon S3 console](https://console.aws.amazon.com/s3/). Choose the bucket you want to delete from the list, so that the whole bucket row is selected. Choose delete bucket, type the name of the bucket, and click "Confirm."

For more information about deleting folders and buckets, go to [How Do I Delete an S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/delete-bucket.html) in the Amazon Simple Storage Service Getting Started Guide.

You can view your billing information at any time by clicking on your account name on the upper right corner of the console and go to **My Billing Dashboard**.

![](https://video.udacity-data.com/topher/2018/December/5c1a1eb8_aws-billing/aws-billing.png)

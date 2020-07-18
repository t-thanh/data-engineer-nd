# Implementing Data Warehouses on AWS

## [Lesson Introduction](https://www.youtube.com/watch?v=dUGo0bvo4MQ)

## [Data Warehouse: A Closer Look](https://www.youtube.com/watch?v=EJiFq7iKvNI)

## [Choices for Implementing a Data Warehouse](https://www.youtube.com/watch?v=wnPf5iw_HuA)

## [DWH Dimensional Model Storage on AWS](https://www.youtube.com/watch?v=ERA2pMIJi7Q)

## [Amazon Redshift Technology](https://www.youtube.com/watch?v=zAQuOCI9bFE)

## [Amazon Redshift Architecture](https://www.youtube.com/watch?v=uAyHUF6s3fg)

## [Redshift Architecture Example](https://www.youtube.com/watch?v=jHEgPY7eDqE)

## [SQL to SQL ETL](https://www.youtube.com/watch?v=UHhoaojC8gE)

## [SQL to SQL ETL - AWS Case](https://www.youtube.com/watch?v=EWgFtSl83J4)

## [Redshift & ETL in Context](https://www.youtube.com/watch?v=JQEAYabMr20)

## [Ingesting at Scale](https://www.youtube.com/watch?v=maAfudoixmE)

## [Redshift ETL Examples](https://www.youtube.com/watch?v=i3a71j8mNjI)

## [Redshift ETL Continued](https://www.youtube.com/watch?v=T-eSqvmuf6w)

## [Redshift Cluster Quick Launcher](https://www.youtube.com/watch?v=8Gv6bOY5fvw)

### TO-DO: Create a Redshift Cluster Using the Quick Launcher
- Follow the video below to create a Redshift cluster.
- Use the query editor to create a table and insert data.
- Delete the cluster.

**IMPORTANT NOTICE:** AWS UI is subject to change on a regular basis and we advise students to refer to AWS documentation. As of June 2020, the UI for setting up the Redshift cluster has slightly changed. You can find the updated documentation on building and launching a Redshift cluster [here](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-launch-sample-cluster.html).

## Exercise 1: Launch Redshift Cluster

### Launching a Redshift Cluster in the AWS Console

- Follow the instructions below to create a Redshift cluster
- Use the query editor to create a table and insert data
- Delete the cluster

Note: The steps below were introduced in lesson 2. You can use the IAM role and security group created in the last lesson.

#### Launch a Redshift Cluster

**WARNING**: The cluster that you are about to launch will be live, and you will be charged the standard Amazon Redshift usage fees for the cluster until you delete it. **Make sure to delete your cluster each time you're finished working to avoid large, unexpected costs.** Instructions on deleting your cluster are included on the last page. You can always launch a new cluster, so don't leave your Redshift cluster running overnight or throughout the week if you don't need to.

- Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshift/.](https://console.aws.amazon.com/redshift/)
- On the Amazon Redshift Dashboard, choose **Launch cluster**.

- On the Cluster details page, enter the following values and then choose Continue:
    - **Cluster identifier**: Enter `redshift-cluster`.
    - **Database name**: Enter `dev`.
    - **Database port**: Enter `5439`.
    - **Master user name**: Enter `awsuser`.
    - **Master user password** and **Confirm password**: Enter a password for the master user account.

- On the Node Configuration page, accept the default values and choose **Continue**.

- On the Additional Configuration page, enter the following values:
    - **VPC security groups**: redshift_security_group
    - **Available IAM roles**: myRedshiftRole
Choose **Continue**.

- Review your Cluster configuration and choose **Launch cluster**.

- A confirmation page will appear and the cluster will take a few minutes to finish. Choose Clusters in the left navigation pane to return to the list of clusters.

- On the Clusters page, look at the cluster that you just launched and review the Cluster Status information. Make sure that the Cluster Status is available and the Database Health is healthy before you try to connect to the database later. You can expect this to take 5-10 minutes.

#### Delete a Redshift Cluster

Make sure to delete your cluster each time you're finished working to avoid large, unexpected costs. You can always launch a new cluster, so don't leave it running overnight or throughout the week if you don't need to.

- On the Clusters page of your Amazon Redshift console, click on the box next to your cluster to select it, and then click on Cluster > Delete cluster.

- You can choose No for Create snapshot, check the box that you acknowledge this, and then choose Delete.

- Your cluster will change it's status to deleting, and then disappear from your Cluster list once it's finished deleting. You'll no longer be charged for this cluster.

## [Problems with the Quick Launcher](https://www.youtube.com/watch?v=G0UoVNj88Wk)

## [Infrastructure as Code on AWS](https://www.youtube.com/watch?v=fDCSEGGvF6I)

## [Enabling Programmatic Access fo IaC](https://www.youtube.com/watch?v=IYbpvvLjWf8)

Boto3 is a Python SDK for programmatically accessing AWS. It enables developers to create, configure, and manage AWS services. You can find the documentation for Boto3 [here](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

## [Demo: Infrastructure as Code](https://www.youtube.com/watch?v=1h8KqUMTK5o)

## [Demo: Parallel ETL](https://www.youtube.com/watch?v=ZeFEotdv6Ig)

## [Optimizing Table Design](https://www.youtube.com/watch?v=nJXaqtBfhwI)

## [Distribution Style: Even](https://www.youtube.com/watch?v=AJjEZbnxabU)

## [Distribution Style: All](https://www.youtube.com/watch?v=8ugf27t-z4M)

## [Distribution Syle: Auto](https://www.youtube.com/watch?v=QYodq1oKeSU)

## [Distribution Syle: Key](https://www.youtube.com/watch?v=CtD2dkiBkUk)

## [Sorting Key](https://www.youtube.com/watch?v=wubk59sUZnk)

## Sorting Key Example
## Demo: Table Design
## Conclusion
# Data Pipelines
## [Welcome](https://youtu.be/8X_TAOja-w4)
## AWS Account and Credits

If you are working your way through the Data Engineering Nanodegree, you have probably already set up an AWS account and received your promotional credits earlier in the program.

If not, before you begin this course you should go to the lesson "Introduction to the Cloud and AWS" in the Data Warehouses course and follow the directions there to get yourself set up with AWS.

Once you have your AWS account and credits set up, please continue in this course!

## [What is a Data Pipeline?](https://youtu.be/8-WH7CUdmzc)
### Defining New Terms
The video above includes references to a few terms that you may not be familiar with. Below are some definitions that you might find useful.

#### Extract Transform Load (ETL) and Extract Load Transform (ELT):
"ETL is normally a continuous, ongoing process with a well-defined workflow. ETL first extracts data from homogeneous or heterogeneous data sources. Then, data is cleansed, enriched, transformed, and stored either back in the lake or in a data warehouse.

"ELT (Extract, Load, Transform) is a variant of ETL wherein the extracted data is first loaded into the target system. Transformations are performed after the data is loaded into the data warehouse. ELT typically works well when the target system is powerful enough to handle transformations. Analytical databases like Amazon Redshift and Google BigQ."

Source: [Xplenty.com](https://www.xplenty.com/blog/etl-vs-elt/)

This [Quora post](https://www.quora.com/What-is-the-difference-between-the-ETL-and-ELT) is also helpful if you'd like to read more.

#### What is S3?

"Amazon S3 has a simple web services interface that you can use to store and retrieve any amount of data, at any time, from anywhere on the web. It gives any developer access to the same highly scalable, reliable, fast, inexpensive data storage infrastructure that Amazon uses to run its own global network of web sites."

Source: [Amazon Web Services Documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html).

If you want to learn more, start [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html).

#### What is Kafka?

"Apache Kafka is an **open-source stream-processing software** platform developed by Linkedin and donated to the Apache Software Foundation, written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. Its storage layer is essentially a massively scalable pub/sub message queue designed as a distributed transaction log, making it highly valuable for enterprise infrastructures to process streaming data."

*Source: Wikipedia*.

If you want to learn more, start [here](https://kafka.apache.org/intro).

#### What is RedShift?

"Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. You can start with just a few hundred gigabytes of data and scale to a petabyte or more... The first step to create a data warehouse is to launch a set of nodes, called an Amazon Redshift cluster. After you provision your cluster, you can upload your data set and then perform data analysis queries. Regardless of the size of the data set, Amazon Redshift offers fast query performance using the same SQL-based tools and business intelligence applications that you use today.

If you want to learn more, start [here](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html).

So in other words, S3 is an example of the final data store where data might be loaded (e.g. ETL). While Redshift is an example of a data warehouse product, provided specifically by Amazon.

## [Data Validation](https://youtu.be/Y4N8CQbfExM)

Data Validation is the process of ensuring that data is present, correct & meaningful. Ensuring the quality of your data through automated validation checks is a critical step in building data pipelines at any organization.

## [DAGs and Data Pipelines](https://youtu.be/YcahqfpcDeA)

### Definitions
- **Directed Acyclic Graphs (DAGs)**: DAGs are a special subset of graphs in which the edges between nodes have a specific direction, and no cycles exist. When we say “no cycles exist” what we mean is the nodes cant create a path back to themselves.
- **Nodes**: A step in the data pipeline process.
- **Edges**: The dependencies or relationships other between nodes.

![](https://video.udacity-data.com/topher/2019/February/5c5f5b00_capture/capture.png)
Diagram of a Directed Acyclic Graph

### Common Questions
#### Are there real world cases where a data pipeline is not DAG?

It is possible to model a data pipeline that is not a DAG, meaning that it contains a cycle within the process. However, the vast majority of use cases for data pipelines can be described as a directed acyclic graph (DAG). This makes the code more understandable and maintainable.

#### Can we have two different pipelines for the same data and can we merge them back together?

Yes. It's not uncommon for a data pipeline to take the same dataset, perform two different processes to analyze the it, then merge the results of those two processes back together.

## [Bikeshare DAG](https://youtu.be/-Z2I5i4bGS8)

## [Introduction to Apache Airflow](https://youtu.be/FNZmWBH2lTw)

"Airflow is a platform to programmatically author, schedule and monitor workflows. Use airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative."

If you'd like to learn more, start [here](https://airflow.apache.org/).

## [Demo 1: Airflow DAGs](https://youtu.be/vtV2qQk4Sc0)

### Tips for Using Airflow's Web Server
- Use Google Chrome to view the Web Server. Airflow sometimes has issues rendering correctly in Firefox or other browers.
- Make sure you toggle the DAG to `On` before you try an run it. Otherwise you'll see your DAG running, but it won't ever finish.

## [Solution 1: Airflow DAGs](https://youtu.be/oLZuImgbugw)

**Callables** can also be thought of as passing functions that can be included as arguments to other functions. Examples of callables are map, reduce, filter. This is a pretty powerful feature of python you can explore more using the resources below. Callables are examples of functional programming that is introduced in an earlier lesson.

Here is the link to the [Python documentation on callables](https://docs.python.org/3.4/library/functools.html).

## [How Airflow Works](https://youtu.be/vltaMg-mC4I)

### Components of Airflow

![](https://video.udacity-data.com/topher/2019/February/5c5f6105_airflow-diagram/airflow-diagram.png)

- **Scheduler** orchestrates the execution of jobs on a trigger or schedule. The Scheduler chooses how to prioritize the running and execution of tasks within the system. You can learn more about the Scheduler from the official [Apache Airflow documentation](https://airflow.apache.org/scheduler.html).
- **Work Queue** is used by the scheduler in most Airflow installations to deliver tasks that need to be run to the **Workers**.
- **Worker** processes execute the operations defined in each DAG. In most Airflow installations, workers pull from the **work queue** when it is ready to process a task. When the worker completes the execution of the task, it will attempt to process more work from the **work queue** until there is no further work remaining. When work in the queue arrives, the worker will begin to process it.
- **Database** saves credentials, connections, history, and configuration. The database, often referred to as the *metadata database*, also stores the state of all tasks in the system. Airflow components interact with the database with the Python ORM, [SQLAlchemy](https://www.sqlalchemy.org/).
- **Web Interface** provides a control dashboard for users and maintainers. Throughout this course you will see how the web interface allows users to perform tasks such as stopping and starting DAGs, retrying failed tasks, configuring credentials, The web interface is built using the [Flask web-development microframework](http://flask.pocoo.org/).

### How Airflow Works

![](https://video.udacity-data.com/topher/2019/February/5c5f8e1d_how-airflow-works/how-airflow-works.png)

#### Order of Operations For an Airflow DAG
- The Airflow Scheduler starts DAGs based on time or external triggers.
- Once a DAG is started, the Scheduler looks at the steps within the DAG and determines which steps can run by looking at their dependencies.
- The Scheduler places runnable steps in the queue.
- Workers pick up those tasks and run them.
- Once the worker has finished running the step, the final status of the task is recorded and additional tasks are placed by the scheduler until all tasks are complete.
- Once all tasks have been completed, the DAG is complete.

## [Building a Data Pipeline](https://youtu.be/vW1A4cTjdks)
### Creating a DAG

Creating a DAG is easy. Give it a name, a description, a start date, and an interval.
```
from airflow import DAG


divvy_dag = DAG(
    'divvy',
    description='Analyzes Divvy Bikeshare Data',
    start_date=datetime(2019, 2, 4),
    schedule_interval='@daily')
```

### Creating Operators to Perform Tasks

**Operators** define the atomic steps of work that make up a DAG. Instantiated operators are referred to as **Tasks**.
```
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_world():
    print(“Hello World”)

divvy_dag = DAG(...)
task = PythonOperator(
    task_id=’hello_world’,
    python_callable=hello_world,
    dag=divvy_dag)
```
### Schedules

**Schedules** are optional, and may be defined with cron strings or Airflow Presets. Airflow provides the following presets:

- `@once` - Run a DAG once and then never again
- `@hourly` - Run the DAG every hour
- `@daily` - Run the DAG every day
- `@weekly` - Run the DAG every week
- `@monthly` - Run the DAG every month
- `@yearly`- Run the DAG every year
- `None` - Only run the DAG when the user initiates it

**Start Date**: If your start date is in the past, Airflow will run your DAG as many times as there are schedule intervals between that start date and the current date.

**End Date**: Unless you specify an optional end date, Airflow will continue to run your DAGs until you disable or delete the DAG.

## [Demo 2: Run the Schedules](https://youtu.be/FyJEXY8h3YE)
## [Solution 2: Run the Schedules](https://youtu.be/nW6Bnrlw3Ys)
## [Operators and Tasks](https://youtu.be/IJKsUQWz_Vo)

### Operators

Operators define the atomic steps of work that make up a DAG. Airflow comes with many Operators that can perform common operations. Here are a handful of common ones:

- `PythonOperator`
- `PostgresOperator`
- `RedshiftToS3Operator`
- `S3ToRedshiftOperator`
- `BashOperator`
- `SimpleHttpOperator`
- `Sensor`

### Task Dependencies

In Airflow DAGs:

- Nodes = Tasks
- Edges = Ordering and dependencies between tasks

Task dependencies can be described programmatically in Airflow using `>>` and `<<`

- `a >> b` means a comes before b
- `a << b` means a comes after b

```
hello_world_task = PythonOperator(task_id=’hello_world’, ...)
goodbye_world_task = PythonOperator(task_id=’goodbye_world’, ...)
...
# Use >> to denote that goodbye_world_task depends on hello_world_task
hello_world_task >> goodbye_world_task
```

Tasks dependencies can also be set with “set_downstream” and “set_upstream”

- `a.set_downstream(b)` means a comes before b
- `a.set_upstream(b)` means a comes after b

```
hello_world_task = PythonOperator(task_id=’hello_world’, ...)
goodbye_world_task = PythonOperator(task_id=’goodbye_world’, ...)
...
hello_world_task.set_downstream(goodbye_world_task)
```

## [Demo 3: Task Dependencies](https://youtu.be/gCnP3MqwEic)
## [Solution: Task Dependencies](https://youtu.be/g7WPth-PbJc)
## [Airflow Hooks](https://youtu.be/2Vkh9rfh6vE)
### Connection via Airflow Hooks

Connections can be accessed in code via hooks. Hooks provide a reusable interface to external systems and databases. With hooks, you don’t have to worry about how and where to store these connection strings and secrets in your code.
```
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator

def load():
# Create a PostgresHook option using the `demo` connection
    db_hook = PostgresHook(‘demo’)
    df = db_hook.get_pandas_df('SELECT * FROM rides')
    print(f'Successfully used PostgresHook to return {len(df)} records')

load_task = PythonOperator(task_id=’load’, python_callable=hello_world, ...)
```

Airflow comes with many Hooks that can integrate with common systems. Here are a few common ones:

- `HttpHook`
- `PostgresHook` (works with RedShift)
- `MySqlHook`
- `SlackHook`
- `PrestoHook`

## [Demo 4: Connections and Hooks](https://youtu.be/VbBALfhw_v8)

### Correction to Video

The instructions in the video are incorrect about the S3 bucket.

You should create two Airflow variables in the UI:

- s3_bucket: udacity-dend
- s3_prefix: data-pipelines

Using this S3 prefix filters the returned S3 keys, so the number of objects displayed for that bucket will be greatly reduced, and you'll avoid the UI freezing.

## Solution 4: Connections and Hooks
Below is the solution for Exercise 4: Connections and Hooks.

```
import datetime
import logging

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.S3_hook import S3Hook


def list_keys():
    hook = S3Hook(aws_conn_id='aws_credentials')
    bucket = Variable.get('s3_bucket')
    prefix = Variable.get('s3_prefix')
    logging.info(f"Listing Keys from {bucket}/{prefix}")
    keys = hook.list_keys(bucket, prefix=prefix)
    for key in keys:
        logging.info(f"- s3://{bucket}/{key}")


dag = DAG(
        'lesson1.exercise4',
        start_date=datetime.datetime.now())

list_task = PythonOperator(
    task_id="list_keys",
    python_callable=list_keys,
    dag=dag
)
```
## [Demo 5: Context and Templating](https://youtu.be/fIWLBsGjW2c)

*Correction*: At timestamp 0.05 in the video above, the ending square bracket is missing. It should be
```
python print(f"Hello {kwargs['execution_date']}")
```

[Here](https://airflow.apache.org/macros.html) is the Apache Airflow documentation on context variables that can be included as kwargs.

Here is a link to a [blog post](https://blog.godatadriven.com/zen-of-python-and-apache-airflow) that also discusses this topic.

### Runtime Variables

Airflow leverages templating to allow users to “fill in the blank” with important runtime variables for tasks.

```
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_date(*args, **kwargs):
    print(f“Hello {kwargs[‘execution_date’]}”)

divvy_dag = DAG(...)
task = PythonOperator(
    task_id=’hello_date’,
    python_callable=hello_date,
    provide_context=True,
    dag=divvy_dag)
```

## [Solution 5: Context and Templating](https://youtu.be/Fe22Ws_OCBI)

The link for the Airflow documentation on context variables has changed since the video was created. Here is the new link: [https://airflow.apache.org/macros.html](https://airflow.apache.org/macros.html)

## [Demo: Exercise 6: Building the S3 to Redshift DAG](https://youtu.be/Wc5WhGwHnZc)
## Solution 6: Build the S3 to Redshift DAG

Below is the solution for Exercise 6: Build the S3 to Redshift Dag.
```
import datetime
import logging

from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

import sql_statements


def load_data_to_redshift(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    redshift_hook.run(sql.COPY_ALL_TRIPS_SQL.format(credentials.access_key, credentials.secret_key))


dag = DAG(
    'lesson1.exercise6',
    start_date=datetime.datetime.now()
)

create_table = PostgresOperator(
    task_id="create_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.CREATE_TRIPS_TABLE_SQL
)

copy_task = PythonOperator(
    task_id='load_from_s3_to_redshift',
    dag=dag,
    python_callable=load_data_to_redshift
)

location_traffic_task = PostgresOperator(
    task_id="calculate_location_traffic",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.LOCATION_TRAFFIC_SQL
)

create_table >> copy_task
copy_task >> location_traffic_task
```
## [Conclusion](https://youtu.be/TRdlpeKrRhM)
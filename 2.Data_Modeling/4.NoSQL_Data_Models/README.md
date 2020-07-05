# NoSQL Data Models

## [Learning Objectives](https://www.youtube.com/watch?v=SnZGJemYgfs)

## [Non-Relational Databases](https://www.youtube.com/watch?v=qF9zF9ls8Yw)

**When Not to Use SQL**:

- **Need high Availability in the data**: Indicates the system is always up and there is no downtime

- **Have Large Amounts of Data**

- **Need Linear Scalability**: The need to add more nodes to the system so performance will increase linearly

- **Low Latency**: Shorter delay before the data is transferred once the instruction for the transfer has been received.

- **Need fast reads and write**

Here is a helpful blog that describes the [different types of NoSQL databases](https://www.xenonstack.com/blog/overview-types-nosql-databases/).

## [Distributed Databases](https://www.youtube.com/watch?v=W0KLTdziin8)

### **Eventual Consistency**:

Over time (if no new changes are made) each copy of the data will be the same, but if there are new changes, the data may be different in different locations. The data may be inconsistent for only milliseconds. There are workarounds in place to prevent getting stale data.

### **Commonly Asked Questions**:

#### **What does the network look like? Can you share any examples?**

In Apache Cassandra every node is connected to every node -- it's peer to peer database architecture.

#### **Is data deployment strategy an important element of data modeling in Apache Cassandra?**

Deployment strategies are a great topic, but have very little to do with data modeling. Developing deployment strategies focuses on determining how many clusters to create or determining how many nodes are needed. These are topics generally covered under database architecture, database deployment and operations, which we will not cover in this lesson. Here is a useful link to learn more about it for [Apache Cassandra](https://docs.datastax.com/en/dse-planning/doc/).

In general, the size of your data and your data model can affect your deployment strategies. You need to think about how to create a cluster, how many nodes should be in that cluster, how to do the actual installation. More information about deployment strategies can be found on this DataStax [documentation page](https://docs.datastax.com/en/dse-planning/doc/)

### **Citation for above slides:**

Here is the [Wikipedia page](https://en.wikipedia.org/wiki/Eventual_consistency) cited in the slides.

### **Cassandra Architecture**

We are not going into a lot of details about the Apache Cassandra Architecture. However, if you would like to learn more about it for your job, here are some links that you may find useful.

#### **Apache Cassandra Data Architecture**:

- [Understanding the architecture](https://docs.datastax.com/en/cassandra/3.0/cassandra/architecture/archTOC.html)

- [Cassandra Architecture](https://www.tutorialspoint.com/cassandra/cassandra_architecture.htm)

The following link will go more in-depth about the Apache Cassandra Data Model, how Cassandra reads, writes, updates, and deletes data.

- [Cassandra Documentation](https://docs.datastax.com/en/cassandra/3.0/cassandra/dml/dmlIntro.html)

## [CAP Theorem](https://www.youtube.com/watch?v=Ms9NcbSoFnA)

### CAP Theorem:

- **Consistency**: Every read from the database gets the latest (and correct) piece of data or an error

- **Availability**: Every request is received and a response is given -- without a guarantee that the data is the latest update

- **Partition Tolerance**: The system continues to work regardless of losing network connectivity between nodes

### Additional Resource:

You can also check out this [Wikipedia page](https://en.wikipedia.org/wiki/CAP_theorem) on the CAP theorem.

### Commonly Asked Questions:

#### Is Eventual Consistency the opposite of what is promised by SQL database per the ACID principle?

Much has been written about how Consistency is interpreted in the ACID principle and the CAP theorem. Consistency in the ACID principle refers to the requirement that only transactions that abide by constraints and database rules are written into the database, otherwise the database keeps previous state. In other words, the data should be correct across all rows and tables. However, consistency in the CAP theorem refers to every read from the database getting the latest piece of data or an error.
To learn more, you may find this discussion useful:

- [Discussion about ACID vs. CAP](https://www.voltdb.com/blog/2015/10/22/disambiguating-acid-cap/)

#### Which of these combinations is desirable for a production system - Consistency and Availability, Consistency and Partition Tolerance, or Availability and Partition Tolerance?

As the CAP Theorem Wikipedia entry says, "The CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability." So there is no such thing as Consistency and Availability in a distributed database since it must always tolerate network issues. You can only have Consistency and Partition Tolerance (CP) or Availability and Partition Tolerance (AP). Remember, relational and non-relational databases do different things, and that's why most companies have both types of database systems.

#### Does Cassandra meet just Availability and Partition Tolerance in the CAP theorem?

According to the CAP theorem, a database can actually only guarantee two out of the three in CAP. So supporting Availability and Partition Tolerance makes sense, since Availability and Partition Tolerance are the biggest requirements.

#### If Apache Cassandra is not built for consistency, won't the analytics pipeline break?

If I am trying to do analysis, such as determining a trend over time, e.g., how many friends does John have on Twitter, and if you have one less person counted because of "eventual consistency" (the data may not be up-to-date in all locations), that's OK. In theory, that can be an issue but only if you are not constantly updating. If the pipeline pulls data from one node and it has not been updated, then you won't get it. Remember, in Apache Cassandra it is about **Eventual Consistency**.

## [Denormalization in Apache Cassandra](https://www.youtube.com/watch?v=zvl4nzqJJYc)

### Data Modeling in Apache Cassandra:

- Denormalization is not just okay -- it's a must

- Denormalization must be done for fast reads

- Apache Cassandra has been optimized for fast writes

- ALWAYS think Queries first

- One table per query is a great strategy

- Apache Cassandra does not allow for JOINs between tables

### Commonly Asked Questions:

#### I see certain downsides of this approach, since in a production application, requirements change quickly and I may need to improve my queries later. Isn't that a downside of Apache Cassandra?

In Apache Cassandra, you want to model your data to your queries, and if your business need calls for quickly changing requirements, you need to create a new table to process the data. That is a requirement of Apache Cassandra. If your business needs calls for ad-hoc queries, these are not a strength of Apache Cassandra. However keep in mind that it is easy to create a new table that will fit your new query.

Additional Resource:

Here is a reference to the DataStax documents on [Apache Cassandra](https://docs.datastax.com/en/dse/6.7/cql/cql/ddl/dataModelingApproach.html)

## [CQL](https://www.youtube.com/watch?v=XlUtr6T2FuA)

## [Demo 1](https://www.youtube.com/watch?v=k8uQ8moKFPk)

Here is the link to the demo [notebook](https://video.udacity-data.com/topher/2019/March/5c9f8588_lesson-3-demo-1-2-queries-2-tables/lesson-3-demo-1-2-queries-2-tables.ipynb)
 
## Exercise 1

## Exercise 1 Solution

## Primary Key

## Quiz: Primary Key

## Demo 2

## Exercise 2

## Exercise 2: Solution

## Clustering Columns

## Demo 3

## Exercise 3

## Exercise 3: Solution

## WHERE Clause

## Demo 4

## Exercise 4

## Lesson Wrap Up

## Course Wrap Up
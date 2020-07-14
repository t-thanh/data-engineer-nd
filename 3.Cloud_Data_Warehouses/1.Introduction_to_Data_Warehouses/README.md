# Introduction to Data Warehouses

## [Course Introduction](https://www.youtube.com/watch?v=W5xxQEk4yZM)

### Outline

- Introduction to Data Warehouses
- Introduction to the Cloud and AWS
- Implementing Data Warehouses on AWS

## [Lesson Introduction](https://www.youtube.com/watch?v=Ahg8ehawvfc)

### Objective
to understand the purpose, architecture, and technologies used in a data warehouse.

### Prerequisites

- Relational database design & SQL
- Programming in Python
- Basic familiarity with dimensional modeling

### Lesson Overview

- What is a Data Warehouse? A Business Perspective
- What is a Data Warehouse? A Technical Perspective
- Dimensional Modeling (Recap)
- DWH Architecture
- OLAP Cubes
- DWH Storage Technology

## [Data Warehouse: Business Perspective](https://www.youtube.com/watch?v=wMN48PtXnow)

### What Is A Data Warehouse? A Business Perspective
You are in charge of a retailer’s data infrastructure. Let’s look at some business activities.

- Customers should be able to find goods & make orders
- Inventory Staff should be able to stock, retrieve, and re-order goods
- Delivery Staff should be able to pick up & deliver goods
- HR should be able to assess the performance of sales staff
- Marketing should be able to see the effect of different sales channels
- Management should be able to monitor sales growth

Ask yourself:

- Can I build a database to support these activities?
- Are all of the above questions of the same nature?

Let's take a closer look at details that may affect your data infrastructure.

- Retailer has a nation-wide presence → **Scale?**
- Acquired smaller retailers, brick & mortar shops, online store → **Single database? Complexity?**
- Has support call center & social media accounts → **Tabular data?**
- Customers, Inventory Staff and Delivery staff expect the system to be fast & stable → **Performance**
- HR, Marketing & Sales Reports want a lot information but have not decided yet on everything they need → **Clear Requirements?**

Ok, maybe one single relational database won’t suffice :)

## [Operational vs. Analytical Processes](https://www.youtube.com/watch?v=2WZaa1jGTE8)
## [Data Warehouse: Technical Perspective](https://www.youtube.com/watch?v=tGO-aGPyt68)
## Dimensional Modeling
### [Dimentional Modeling (Recap)](https://www.youtube.com/watch?v=ony5hGkSo78)
### [Example](https://www.youtube.com/watch?v=GR29jiNw0XE)
## [ETL Demo: Step 1 & 2](https://www.youtube.com/watch?v=qDbyxiKFrLE)

## ETL Demo: Step 3

### [Part 1](https://www.youtube.com/watch?v=AckKPNjW17A)
### [Part 2](https://www.youtube.com/watch?v=SRHmqx4fGmU)
### [Part 3](https://www.youtube.com/watch?v=Ls1-xCiqHiI)

## [ETL Demo: Step 4](https://www.youtube.com/watch?v=HHuhptPD7Kc)

## [ETL Demo: Step 5](https://www.youtube.com/watch?v=IimfrD6lnu8)

## [ETL Demo: Step 6](https://www.youtube.com/watch?v=fHAALyRwGC0)

## [DWH Architecture: Kimball's Bus Architecture](https://www.youtube.com/watch?v=cBK4T9LhD-A)
## [DWH Architecture: Independent Data Marts](https://www.youtube.com/watch?v=5ItLNcoZMSs)
## [DWH Architecture: CIF](https://www.youtube.com/watch?v=mVqWU7jzbAc)
## [DWH Architecture: Hybrid Bus & CIF](https://www.youtube.com/watch?v=6DnHS6gVqIY)
## [OLAP Cubes](https://www.youtube.com/watch?v=modd7NmChic)
## [OLAP Cubes: Roll-Up and Drill Down](https://www.youtube.com/watch?v=scJR8EpV82A)
## [OLAP Cubes: Slice and Dice](https://www.youtube.com/watch?v=ezSrpOeHG1Y)
## [OLAP Cubes: Query Optimization](https://www.youtube.com/watch?v=pe0-17CSuLs)
## OLAP Cubes Demo: Slicing & Dicing
### [Introduction](https://www.youtube.com/watch?v=ZyHRUErDOrQ)
### [Slicing](https://www.youtube.com/watch?v=_9zZ_vIZZ0A)
### [Dicing](https://www.youtube.com/watch?v=j9umvBak-jY)
## OLAP Cubes Demo: Roll-Up & Drill-Down
### [Roll-Up](https://www.youtube.com/watch?v=eUGQrKKiQ2M)
### [Drill-Down](https://www.youtube.com/watch?v=JPtPNtb3vnE)
## [OLAP Cubes Demo: Grouping Sets](https://www.youtube.com/watch?v=58nWFb-AJU8)
## [OLAP Cubes Demo: CUBE](https://www.youtube.com/watch?v=fMkaZuxCCqw)
## [Data Warehouse Technologies](https://www.youtube.com/watch?v=v7QX4w2kC-4)

Here are links to the three books referenced in the video:

- [The Data Warehouse Toolkit: The Complete Guide to Dimensional Modeling (Kimball)](https://www.amazon.com/Data-Warehouse-Toolkit-Complete-Dimensional/dp/0471200247)
- [Building the Data Warehouse (Inmon)](https://www.amazon.com/Building-Data-Warehouse-W-Inmon/dp/0764599445)
- [Building a Data Warehouse: With Examples in SQL Server (Rainardi)](https://www.amazon.com/Building-Data-Warehouse-Examples-Experts/dp/1590599314)
## [Demo: Column format in ROLAP](https://www.youtube.com/watch?v=ELlnfNRn8Rw)
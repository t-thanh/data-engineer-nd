# Data Engineering Capstone Project
### US I94 Immigration Dataset

## Overview
The goal of this project is the build data warehouse system in AWS cloud environment in Redshift Cluster to analyze data on immigration to the United States and airport codes

## Dataset overview

- **I94 Immigration Data**: This data comes from the US National Tourism and Trade Office ([link](https://travel.trade.gov/research/reports/i94/historical/2016.html)). `immigration_data_sample.csv` contains the sample data.

- **U.S. City Demographic Data**: This data comes from [OpenSoft](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/). This dataset contains information about the demographics of all US cities and census-designated places with a population greater or equal to 65,000. This data comes from the US Census Bureau's 2015 American Community Survey.

- **Airport Code Table**: This data comes from [ourairports](http://ourairports.com/data/airports.csv). It is a simple table of airport codes and corresponding cities. It contains the list of all airport codes, the attributes are identified in datapackage description. Some of the columns contain attributes identifying airport locations, other codes (IATA, local if exist) that are relevant to identification of an airport.

## Project Files

- `capstone_notebook.ipynb`: The notebook to reads data, processes that data using **Spark**, writes in **S3**, and copy to **Amazon Redshift**.

- `create_redshift.py`: script for create environment in AWS.

- `create_tables.py`: script for **fact** and **dimension tables** for the start schema in Redshift.

- `dwh.cfg`: Config file for put your config of environment AWS.

- `README.md`: Readme file

- `remove_redshift.py`: script for remove environment in AWS.

- `sql_queries.py`: sql queries for dropping, creating and inserting the tables.


## Instructions

- Give your AWS **region**, **key** and **secret** in SECTION **AWS** into the config file `dwh.cfg`

- Run the file `capstone_notebook.ipynb`

**Attention** - To delete Redshift Cluster on AWS, uncomment and run last cell in notebook jupyter
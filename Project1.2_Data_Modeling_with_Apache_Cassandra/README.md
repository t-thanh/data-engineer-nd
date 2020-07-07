# Project: Data Modeling with Cassandra

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

## Objective

To create an Apache Cassandra database which can create queries on song play data to answer the questions and to test the database by running gqueries given by the analytics team from Sparkify to create the results.


## Database design and ETL pipeline

The data is ingested from source folders `event_data` in form of csv files using pandas library in Python. Data is further filtered, cleaned and recorde using Cassandra CQL and Python statements and commands. The tables are created to answer below questions.

## Query examples:

 1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4
 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
 3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

## Instruction: Run notebook in jupyter notebook

1. to process the `event_datafile_new.csv` dataset to create a denormalized dataset
2. to model the data tables for the above queries
3. to load the data into tables created in Apache Cassandra and run queries
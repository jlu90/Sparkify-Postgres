# Sparkify: Creating a Relational Data Model using postgreSQL  

### Author: Jocelyn Lutes, M.S.

### Background
Sparkify is a new startup that is looking to revolutionize music streaming through the use of its Sparkify Music App. The analytics team at Sparkify is interested in understanding user behavior on the app (particularly which songs users are listening to). Currently, there is no easy way for the analytics team to retrieve the data that they need to answer their questions. 

**Problem Statement**: For this project, the data engineering team has been tasked to build a relational database that is optimized for queries on song play analysis.

### Contents of Repository
* [Data Folder]()
* [sql_queries.py]() - Python script containing SQL queries to create tables, insert data into tables, drop tables, and perform other queries
* [create_tables.py]() - Python script that creates a postgres database containing empty tables
* [etl.py]() - Python script that extracts data from JSON files, transforms it to the appropriate data type or format, and loads it into a SQL table
* [test.ipynb]() - Jupyter Notebook containing sample queries

### Instructions for  Repository
1. Run `create_tables.py` to create database and tables
2. Run `etl.py` to load data into appropriate tables
3. Run cells in `test.ipynb` to test that data was loaded correctly

### Summary of Workflow
#### Data
* Song Dataset (JSON) - Contains data about a song, including song_id, title, song_duration, artist_id, artist_name, and information about the artist's location.
* Log Dataset (JSON) - Contains simulated data related to a music streaming event, including user information and details about the session
#### Relational Data Schema
For this database, a star schema was used in which a fact table containing information about a listening session was related to four dimensional tables that provided expanded information about the session.



# Sparkify: Creating a Relational Data Model using PostgreSQL  

### Author: Jocelyn Lutes
### Project Notes: Created as part of Udacity's Data Engineering Nanodegree

### Background
Sparkify is a new startup that is looking to revolutionize music streaming through the use of its Sparkify Music App. The analytics team at Sparkify is interested in understanding user behavior on the app (particularly which songs users are listening to). Currently, there is no easy way for the analytics team to retrieve the data that they need to answer their questions. 

**Problem Statement**: For this project, the data engineering team has been tasked to build a relational database that is optimized for queries on song play analysis.

### Contents of Repository
* Data
* sql_queries.py - Python script containing SQL queries to create tables, insert data into tables, drop tables, and perform other queries
* create_tables.py - Python script that creates a postgres database containing empty tables
* etl.py - Python script that extracts data from JSON files, transforms it to the appropriate data type or format, and loads it into a SQL table
* test.ipynb - Jupyter Notebook containing sample queries

### Instructions for  Repository
1. Run `create_tables.py` to create database and tables
2. Run `etl.py` to load data into appropriate tables
3. Run cells in `test.ipynb` to test that data was loaded correctly

* **NOTE**: To reset data tables, `create_tables.py` should **ALWAYS** be run before running `etl.py`

### Summary of Workflow
#### Data
* Song Dataset (JSON) - Contains data about a song, including song_id, title, song_duration, artist_id, artist_name, and information about the artist's location.
* Log Dataset (JSON) - Contains simulated data related to a music streaming event, including user information and details about the session
#### Relational Data Schema
* For this database, a star schema was used in which a fact table containing information about a listening session was related to four dimensional tables that provided expanded information about the session.  

* **NOTE:** For description of tables, see [`schema.md`](https://github.com/jlu90/Sparkify-Postgres/blob/main/schema.md).

#### ETL Pipeline
1. Create postgreSQL database named ***sparkifydb***
2. Create fact and dimension tables in ***sparkifydb*** according to [schema](https://github.com/jlu90/Sparkify-Postgres/blob/main/schema.md)
3. Extract data necessary for the songs table from song dataset using Python and pandas
4. Use psycopg2 and `song_table_insert` from `sql_queries.py` to insert song data into songs table
5. Extract data necessary for the artists table from song dataset using Python and pandas
6. Use psycopg2 and `artist_table_insert` from `sql_queries.py` to insert artist data into artist table
7. Extract time information from the log dataset and transform it into a pandas datetime object
8.  Use psycopg2 and `time_table_insert` from `sql_queries.py` to insert time data into time table
9. Extract user information from the log dataset
10. Use psycopg2 and `user_table_insert` from `sql_queries.py` to insert user data into user table
11. Use `select_song` query from `sql_queries.py` to retrieve the song ID and artist ID for songs in the log data set and extract the remaining songplay data from the log data set
12. Use psycopg2 and  the `songplay_table_insert` from `sql_queries.py` to insert data related to the songplay session into the songplay table

#### Sample Queries
```sql
SELECT * FROM songs
LIMIT 5;
```

```sql
SELECT * FROM songplays
WHERE song_id IS NOT NULL;
```






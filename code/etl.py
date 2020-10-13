import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    ''' 
    - Converts opens JSON file from filepath and stores data in pandas data frame
    - Inserts song data into song table
    - Inserts artist data into artist table
    '''
    # open song file
    data = pd.read_json(filepath, typ = 'series') # Must open as a series and then convert to df
    df = pd.DataFrame([data])

    # insert song record
    song_df = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    song_data = list(song_df.values[0])
    print(song_data)
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_df = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]
    artist_data = list(artist_df.values[0])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    - Reads JSON file from filepath into a pandas data frame
    - Filters data to only include 'Next Song' actions
    - Extracts time information and inserts it into the time table
    - Extracts user information and inserts it into user table
    - Finds song_id and artist_id for songs in log data set
    - Extracts songplay information and inserts it into songplay table
    '''
    # open log file
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit = 'ms')

    # extract datetime units
    timestamp = list(t.dt.time.values)
    hour = list(t.dt.hour.values)
    day = list(t.dt.day.values)
    week = list(t.dt.isocalendar().week.values) # CANNOT USE t.dt.week.values because it is deprecated in my version of Python
    month = list(t.dt.month.values)
    year = list(t.dt.year.values)
    weekday = list(t.dt.day_name().values)
    
    # insert time data records
    time_data = [timestamp, hour, day, week, month, year, weekday]
    column_labels = ['timestamp', 'hour', 'day', 'week', 'month', 'year', 'weekday']

    time_dict = {}
    for i in range(0, len(time_data)):
        time_dict[column_labels[i]] = time_data[i]    

    time_df = pd.DataFrame(time_dict)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        if results:
            songid = results[0]
            artistid = results[1]
        else:
            songid = None
            artistid = None 
        # songid, artistid = results if results else None, None (NOTE: TUPLE WAS NOT UNPACKING)

        # insert songplay record
        songplay_data = (t[i], row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    - Aggregates all JSON files from a directory into a list
    - Iterates over list of files and applies a processing function to those files
    - Reports progress as it runs
    '''
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''
    - Connects to sparkifydb
    - Applies song processing to song data set -> Inserts data into songs and artists tables
    - Applies log processing to log data set -> Inserts data into time, users, and songplays tables
    '''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb")
    cur = conn.cursor()

    process_data(cur, conn, filepath='../data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='../data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
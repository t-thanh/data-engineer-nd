import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE SCHEMA

schema_create = ("""
CREATE SCHEMA IF NOT EXISTS sparkify;
SET search_path TO sparkify;
""")

# CREATE TABLES

staging_events_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_events (
    artist          VARCHAR,
    auth            VARCHAR,
    firstName       VARCHAR,
    gender          VARCHAR,
    itemInSession   INTEGER,        
    lastName        VARCHAR,
    length          FLOAT,
    level           VARCHAR,
    location        VARCHAR,
    method          VARCHAR,
    page            VARCHAR,
    registration    VARCHAR,
    sessionId       INTEGER,
    song            VARCHAR,
    status          INTEGER,
    ts              TIMESTAMP,
    userAgent       VARCHAR,
    userId          FLOAT
);
""");

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
    song_id             VARCHAR,
    num_songs           INTEGER,
    title               VARCHAR,
    artist_name         VARCHAR,
    artist_latitude     FLOAT,
    year                INTEGER,
    duration            FLOAT,
    artist_id           VARCHAR,
    artist_longitude    FLOAT,
    artist_location     VARCHAR
);
""");

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id INTEGER IDENTITY(1,1) DISTKEY, 
    start_time  TIMESTAMP NOT NULL, 
    user_id     INTEGER NOT NULL, 
    level       VARCHAR NOT NULL, 
    song_id     VARCHAR NOT NULL SORTKEY, 
    artist_id   VARCHAR NOT NULL, 
    session_id  INTEGER NOT NULL, 
    location    VARCHAR, 
    user_agent  VARCHAR
);
""");

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id     INTEGER NOT NULL DISTKEY, 
    first_name  VARCHAR NOT NULL, 
    last_name   VARCHAR NOT NULL, 
    gender      VARCHAR NOT NULL, 
    level       VARCHAR NOT NULL
);
""");

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id     VARCHAR DISTKEY, 
    title       VARCHAR NOT NULL, 
    artist_id   VARCHAR NOT NULL SORTKEY, 
    year        INTEGER, 
    duration    FLOAT
);
""");

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id   VARCHAR DISTKEY, 
    name        VARCHAR NOT NULL SORTKEY, 
    location    VARCHAR, 
    latitude    FLOAT, 
    longitude   FLOAT
);  
""");

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time  TIMESTAMP DISTKEY, 
    hour        INTEGER, 
    day         INTEGER, 
    week        INTEGER, 
    month       INTEGER, 
    year        INTEGER, 
    weekday     INTEGER
);
""");

# STAGING TABLES

staging_events_copy = ("""
    COPY staging_events
    FROM {}
    iam_role '{}'
    region 'us-west-2'
    COMPUPDATE OFF 
    TIMEFORMAT as 'epochmillisecs' 
    FORMAT AS JSON {};
""").format(config["S3"]["LOG_DATA"], config["IAM_ROLE"]["ARN"], config["S3"]["LOG_JSONPATH"])

staging_songs_copy = ("""
    COPY staging_songs
    FROM {}
    iam_role '{}'
    region 'us-west-2'
    COMPUPDATE OFF
    FORMAT AS JSON 'auto';
""").format(config["S3"]["SONG_DATA"], config["IAM_ROLE"]["ARN"])

# FINAL TABLES

songplay_table_insert = ("""
INSERT INTO songplays 
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
SELECT DISTINCT 
    TO_TIMESTAMP(TO_CHAR(s_e.ts, '9999-99-99 99:99:99'), 'YYYY-MM-DD HH24:MI:SS') AS start_time,
    s_e.userId      AS user_id,
    s_e.level       AS level,
    s_s.song_id     AS song_id,
    s_s.artist_id   AS artist_id,
    s_e.sessionId   AS session_id,
    s_e.location    AS location,
    s_e.userAgent   AS user_agent
FROM staging_events s_e
JOIN staging_songs s_s ON s_s.title = s_e.song AND s_s.artist_name = s_e.artist;
""")

user_table_insert = ("""
INSERT INTO users 
    (user_id, first_name, last_name, gender, level) 
SELECT DISTINCT 
    userId      AS user_id,
    firstName   AS first_name,
    lastName    AS last_name,
    gender      AS gender,
    level       AS level
FROM staging_events
WHERE userId IS NOT NULL;
""")

song_table_insert = ("""
INSERT INTO songs 
    (song_id, title, artist_id, year, duration) 
SELECT DISTINCT 
    song_id     AS song_id,
    title       AS title,
    artist_id   AS artist_id,
    year        AS year,
    duration    AS duration
FROM staging_songs
WHERE song_id IS NOT NULL;
""")

artist_table_insert = ("""
INSERT INTO artists 
    (artist_id, name, location, latitude, longitude) 
SELECT DISTINCT 
    artist_id           AS artist_id,
    artist_name         AS name,
    artist_location     AS location,
    artist_latitude     AS latitude,
    artist_longitude    AS longitude
FROM staging_songs
WHERE artist_id IS NOT NULL;
""")

time_table_insert = ("""
INSERT INTO time 
    (start_time, hour, day, week, month, year, weekday)
SELECT DISTINCT ts,
    EXTRACT(hour from ts),
    EXTRACT(day from ts),
    EXTRACT(week from ts),
    EXTRACT(month from ts),
    EXTRACT(year from ts),
    EXTRACT(weekday from ts)
FROM staging_events
WHERE ts IS NOT NULL;
""")

# QUERY LISTS

create_table_queries = [schema_create, staging_events_table_create,
                        staging_songs_table_create, songplay_table_create,
                        user_table_create, song_table_create, 
                        artist_table_create, time_table_create]

drop_table_queries = [schema_create, staging_events_table_drop, 
                      staging_songs_table_drop, songplay_table_drop, 
                      user_table_drop, song_table_drop, 
                      artist_table_drop, time_table_drop]

copy_table_queries = [schema_create, staging_events_copy, staging_songs_copy]

insert_table_queries = [schema_create, songplay_table_insert, user_table_insert,
                        song_table_insert, artist_table_insert, time_table_insert]
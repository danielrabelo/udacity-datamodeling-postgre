# DROP TABLES
songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES
songplay_table_create = ("""
create table if not exists songplays (
    songplay_id integer,
    start_time timestamp,
    user_id varchar(50),
    level varchar(100),
    song_id varchar(100),
    artist_id varchar(100),
    session_id integer,
    location varchar(100),
    user_agent varchar(100)
);
comment on table songplays is 'Records in log data associated with song plays i.e.';
""")

user_table_create = ("""
create table if not exists users (
    user_id varchar(50),
    first_name varchar(50),
    last_name varchar(100),
    gender varchar(10),
    level varchar(100)
);
comment on table users is 'Users in the app.';
""")

song_table_create = ("""
create table if not exists songs (
    song_id varchar(100),
    title varchar(100),
    artist_id varchar(100),
    year smallint,
    duration numeric
);
comment on table songs is 'Songs in music database.';
""")

artist_table_create = ("""
create table if not exists artists (
    artist_id varchar(100),
    name varchar(100),
    location varchar(100),
    latitude varchar(30),
    longitude varchar(30)
);
comment on table artists is 'Artists in music database.';
""")

time_table_create = ("""
create table if not exists time (
    start_time timestamp,
    hour varchar(10),
    day varchar(10),
    week varchar(15),
    month varchar(20),
    year smallint,
    weekday varchar(20)
);
comment on table time is 'Timestamps of records in songplays broken down into specific units';
""")

# INSERT RECORDS
songplay_table_insert = ("""
insert into songplays (
    songplay_id,
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
insert into users (
    user_id,
    first_name,
    last_name,
    gender,
    level
)
values (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
insert into songs (
    song_id,
    title,
    artist_id,
    year,
    duration
)
values (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
insert into artists (
    artist_id,
    name,
    location,
    latitude,
    longitude
)
values (%s, %s, %s, %s, %s)
""")

time_table_insert = ("""
insert into time (
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
)
values (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS
song_select = ("""
select 
    a.song_id,
    b.artist_id
from 
    songs a
inner join artists b
        on a.artist_id = b.artist_id
where 
    a.title = %s and b.name = %s /*and a.duration = %s*/
;
""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
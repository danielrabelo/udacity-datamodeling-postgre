# Data Engineering Nanodegree
This project loads data from music streaming .json files and inserts it into postgresql in a relational model.

**Prerequisites:**
 - PostgreSQL and Python3.x

**Step 1** - Create tables in to PostgreSQL 
```
python create_tables.py
```
**Step 2** - Load data from .json files into tables 
```
python etl.py
```
**Step 3** - Test if records successfully added into tables
Run jupyter notebook test.ipynb file.

## Project tables
**Tables**
 - songs
 - artists
 - time
 - users
 - songplays
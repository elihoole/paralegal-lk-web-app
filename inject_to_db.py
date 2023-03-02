# read full_table_of_cases.csv and inject to db.sqlite3

import csv
import sqlite3
import pandas as pd

# connect by deleting db.sqlite3 if exists

import os


if os.path.exists("db.sqlite3"):
    print("db.sqlite3 exists, deleting it...")
    os.remove("db.sqlite3")

conn = sqlite3.connect("db.sqlite3")

col_names = ["date", "casenumber", "nameofparties", "link"]

df = pd.read_csv("full_table_of_cases.csv")

df = df[col_names]

# create a column named id and make it the index

df["id"] = df.index

print(df.head(5))

print(df.keys())

df.to_sql("pages_case", conn, if_exists="replace", index=False)

conn.close()

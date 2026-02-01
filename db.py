import sqlite3
from datetime import date, datetime

### Data center ###

conn = sqlite3.connect('db/data.db')
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS transactions (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               amount FLOAT NOT NULL,
               category INTEGER NOT NULL,
               date TEXT NOT NULL,
               description TEXT)
""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS recurring (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               amount FLOAT NOT NULL,
               description TEXT NOT NULL)
""")
conn.commit()
conn.close()

# todo
def insert_recurring(amount: float, date: date, description: str):
    return True

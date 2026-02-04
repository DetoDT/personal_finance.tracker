import sqlite3
from datetime import date, datetime

### Data center ###

path = 'db/data.db'

conn = sqlite3.connect(path)
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS transactions (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               amount FLOAT NOT NULL,
               category INTEGER NOT NULL,
               date TEXT NOT NULL,
               month_and_year TEXT NOT NULL,
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

def insert_transaction(amount: float, date: date, category: int, description: str='') -> int:
    conn = sqlite3.connect(path) 
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO transactions (amount, date, month_and_year, category, description)
                    values (?, ?, ?, ?, ?)
                    ''', (amount, date, date.strftime('%Y-%m'), category, description))
        conn.commit()
        id = cursor.lastrowid
    except Exception as err:
        print(f'Error inserting new transaction: {err}')
        id = -1

    cursor.close() 
    conn.close()
    if id is None:
        return 0
    return id

# insert recurring payment into db
def insert_recurring(amount: float, date: date, description: str, recurrence: int = 1):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO recurring (amount, date, description, recurrence)
                    values (?, ?, ?, ?)
                    ''', (amount, date, description, recurrence))
        conn.commit()
        id = cursor.lastrowid
    except Exception as err:
        print(f'Error inserting new transaction: {err}')
        id = -1

    cursor.close() 
    conn.close()
    if id is None:
        return 0
    return id

def get_month_transactions(month:date) -> list[sqlite3.Row]:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    query = '''
        SELECT * FROM transactions WHERE month_and_year=?'''
    try:
        cursor.execute(query, (str(month.strftime('%Y-%m')),))
        conn.commit()
        output = cursor.fetchall()
    except Exception as err:
        print(f'Error retrieving data: {err}')
        return []
    cursor.close()
    conn.close()
    return output


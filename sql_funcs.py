import tkinter
import sqlite3
from datetime import datetime
import pandas as pd
import numpy as np
from openpyxl import Workbook






# **************ORIGINAL CONNECTION**************
# conn = dbconnect = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
# c = conn.cursor()

# **************CREATE TABLE COMMAND**************
def createTable():
    conn = dbconnect = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    table = '''
        CREATE TABLE books (
            title VARCHAR(100) NOT NULL,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            date DATE,
            cat VARCHAR(30),
            year INTEGER
        )'''
    c.execute("DROP TABLE IF EXISTS books;")
    c.execute(table)
    conn.close()



# **************ALTER TABLE COMMAND**************
def alterTable():
    conn = dbconnect = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute("ALTER TABLE books ADD COLUMN cat VARCHAR(50);")
    conn.commit()
    conn.close()


# **************HARD CODE IN A ROW**************
def insertRow(a, b, c, d, e):
    conn = dbconnect = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute( "INSERT INTO books (title, first_name, last_name, year, date) VALUES (?, ?, ?, ?, ?);",(a, b, c, d, e))
    conn.commit()
    conn.close()

# **************HARD CODE DELETE ALL ROWS**************
def deleteRows():
    conn = dbconnect = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute("DELETE FROM books;")
    conn.commit()
    conn.close()

# **************CONNECTION COMMIT**************
# conn.commit()

# **************RETRIVE BOOK ROWS**************
def selectRows():
    conn = dbconnect = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    backs = c.execute('''
        SELECT * FROM books
        ''')
    for back in backs:
        print(back)
    conn.close()

# **************ORIGINAL CONNECTION CLOSE**************
# conn.close()

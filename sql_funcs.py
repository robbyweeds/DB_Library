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
  conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  c = conn.cursor()
  list_of_tables = c.execute(
    """SELECT * FROM sqlite_master WHERE type='table'; """).fetchall()
  if list_of_tables == []:
    table = '''
        CREATE TABLE books (
            title VARCHAR(100) NOT NULL,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            input_date VARCHAR(40),
            cat VARCHAR(30),
            year INTEGER
        )'''
    # c.execute("DROP TABLE IF EXISTS books;")
    c.execute(table)
    conn.close()
  else:
    conn.close()



# **************ALTER TABLE COMMAND**************
def alterTable():
  conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  c = conn.cursor()
  c.execute("ALTER TABLE books ADD COLUMN cat VARCHAR(50);")
  conn.commit()
  conn.close()


# **************HARD CODE IN A ROW**************
def insertRow(a, b, c, d, e):
  conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  c = conn.cursor()
  c.execute( "INSERT INTO books (title, first_name, last_name, year, input_date) VALUES (?, ?, ?, ?, ?);",(a, b, c, d, e))
  conn.commit()
  conn.close()

# **************HARD CODE DELETE ALL ROWS**************
def deleteRows():
  conn =  sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  c = conn.cursor()
  c.execute("DELETE FROM books;")
  conn.commit()
  conn.close()

# *************DELETE SPECIFIC ROW**********************
def deleteRow(row):
  conn =  sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  c = conn.cursor()
  c.execute("DELETE FROM books WHERE title = ?;", (row,))
  conn.commit()
  conn.close()

# **************CONNECTION COMMIT**************
# conn.commit()

# **************RETRIVE BOOK ROWS**************
def selectRows():
  conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  c = conn.cursor()
  backs = c.execute('''
      SELECT * FROM books
      ''')
  for back in backs:
      print(back)
  conn.close()

# **************ORIGINAL CONNECTION CLOSE**************
# conn.close()



# **************PRINT ROWS TO CONSOLE**************
def print_rows():
  conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  c = conn.cursor()
  backs = c.execute('''
    SELECT rowid, title, first_name, last_name, cat, year, input_date FROM books
    ''')
  for back in backs:
      print(back)

  conn.close()

# **************GRAB AND PRINT ROWS FROM PANDAS**************
def panda_rows():
  conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  surveys_df = pd.read_sql_query("SELECT * from books", conn)
  print(surveys_df)

  conn.close()


# **************RETRIVE Specific BOOK ROWS**************
def editSingleRow(book, fname, lname, year):
  # conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
  # c = conn.cursor()
  if fname == '' and lname == '':
    conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    print('yearssss')
    reply = c.execute('UPDATE books SET year = ? WHERE title = ?', (year, book))
    conn.close()
  elif fname == '' and year == '': 
    reply = c.execute('UPDATE books SET last_name = ? WHERE title = ?', (lname, book))
  elif year == 0 and lname == '':
    reply = c.execute('UPDATE books SET first_name = ? WHERE title = ?', (fname, book))
  elif fname == '': 
    reply = c.execute('UPDATE books SET year = ?, last_name= ? WHERE title = ?', (year, lname, book))
  elif year == 0:
    reply = c.execute('UPDATE books SET first_name = ?, last_name = ?) WHERE title = ?', (fname, lname, book))
  elif lname == '':
    reply = c.execute('UPDATE books SET first_name = ?, year = ? WHERE title = ?', (fname, year, book)) 
  else:
    reply = c.execute('UPDATE books SET last_name= ?, first_name = ?, year = ? WHERE title = ?', (lname, fname, year, book)) 
  # conn.close()

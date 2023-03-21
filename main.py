import tkinter
import sqlite3
from datetime import datetime
import pandas as pd
import numpy as np
from openpyxl import Workbook

# **************CREATE EXCEL**************
def create_excel():
    conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    surveys_df = pd.read_sql_query("SELECT * from books", conn)
    surveys_df.to_excel('landscape_library_list.xlsx')

    conn.close()

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

createTable()

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

tk = tkinter.Tk()

title1 = tkinter.StringVar()
name1 = tkinter.StringVar()
name2 = tkinter.StringVar()
cat1 = tkinter.StringVar()
year1 = tkinter.StringVar()




tk.geometry('300x350')

tk.title('Book Inventory App')

label1 = tkinter.Label(tk, text='Author First Name: ').grid(row=0, column=0)
entry1 = tkinter.Entry(tk, textvariable=name1).grid(row=0, column=1)
label2 = tkinter.Label(tk, text='Author Last Name: ').grid(row=1, column=0)
entry2 = tkinter.Entry(tk, textvariable=name2).grid(row=1, column=1)
label3 = tkinter.Label(tk, text='Book Title: ').grid(row=2, column=0)
entry3 = tkinter.Entry(tk, textvariable=title1).grid(row=2, column=1)
yearLabel = tkinter.Label(tk, text='Book Year: ').grid(row=3, column=0)
yearEntry = tkinter.Entry(tk, textvariable=year1).grid(row=3, column=1)
text1 = tkinter.Label(tk, text='Categories:').grid(row=4, column=1)
label4 = tkinter.Label(tk, text='Trees and shrubs').grid(row=5, column=0)
entry4 = tkinter.Radiobutton(tk, variable=cat1, value='ornamentals').grid(row=5, column=1)
label5 = tkinter.Label(tk, text='Turf and Weeds').grid(row=6, column=0)
entry5 = tkinter.Radiobutton(tk, variable=cat1, value='turf').grid(row=6, column=1)
label6 = tkinter.Label(tk, text='Insects').grid(row=7, column=0)
entry6 = tkinter.Radiobutton(tk, variable=cat1, value='insects').grid(row=7, column=1)
label7 = tkinter.Label(tk, text='Disease').grid(row=8, column=0)
entry7 = tkinter.Radiobutton(tk, variable=cat1, value='disease').grid(row=8, column=1)

def submit():
    name = name1.get()
    print('The name entered is: ', name)

    conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute("INSERT INTO books (title, first_name, last_name, cat, year) VALUES (?, ? ,?, ?, ?);", (title1.get(), name1.get(), name2.get(), cat1.get(), year1.get()))
    conn.commit()    
    conn.close()
    name1.set('')
    name2.set('')
    title1.set('')
    year1.set('')
    # cat1.set('')

def print_rows():
    conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    backs = c.execute('''
    SELECT rowid, title, first_name, last_name, cat, year FROM books
    ''')

    for back in backs:
        print(back)

    conn.close()


def panda_rows():
    conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    surveys_df = pd.read_sql_query("SELECT * from books", conn)
    print(surveys_df)

    conn.close()


btn1 = tkinter.Button(tk, command=submit, text='SUBMIT').grid(row=9, column=1)
btn2 = tkinter.Button(tk, command=print_rows, text='PRINT ROWS').grid(row=10, column=1)
btn3 = tkinter.Button(tk, command=panda_rows, text='PANDA ROWS').grid(row=11, column=1)
btn4 = tkinter.Button(tk, command=deleteRows, text='DELETE ROWS').grid(row=12, column=1)
btn5 = tkinter.Button(tk, command=create_excel, text='TO EXCEL').grid(row=13, column=1)


tk.mainloop()


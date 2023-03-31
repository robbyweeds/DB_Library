import tkinter
import tkinter.messagebox
import sqlite3
from datetime import datetime
import pandas as pd
import numpy as np
from openpyxl import Workbook
import os


# **************EXCEL QUESTION**************
def askExcel():
  reply = tkinter.messagebox.askyesno('Create Excel', 'Click Yes to Create Excel')
  if reply == True:
    tkinter.messagebox.showinfo('Confirmation', 'Excel Created')
    create_excel()
  else:
    tkinter.messagebox.showinfo('Canceled', 'Excel Creation Canceled')
  

# **************CREATE EXCEL**************
def create_excel():
    if os.path.exists("landscape_library_list.xlsx"):
      os.remove("landscape_library_list.xlsx")
    conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    surveys_df = pd.read_sql_query("SELECT * from books", conn)
    surveys_df.to_excel('landscape_library_list.xlsx')

    conn.close()

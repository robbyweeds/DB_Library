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
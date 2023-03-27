import tkinter
import tkinter.messagebox
import tkinter.font as font
import sqlite3
from datetime import date
import pandas as pd
import numpy as np
from openpyxl import Workbook
from sql_funcs import *
from excel_funcs import *
from tkinter_funcs import *

datenow = str(date.today())
print(datenow)

createTable()


buttoncolor = '#298E69'
bgcolor = '#C4C8FF'

tk = tkinter.Tk()
tk.configure(bg=bgcolor)

labelpad = 10

catfont = font.Font(family='monospace', size=9)
labelfont = font.Font(family='monospace', size=10, weight='bold')
buttonFont = font.Font(family='Helvetica', size=12, weight='bold')

title1 = tkinter.StringVar()
name1 = tkinter.StringVar()
name2 = tkinter.StringVar()
cat1 = tkinter.StringVar()
year1 = tkinter.StringVar()
deleteVar = tkinter.StringVar()
deletewindowtitle = tkinter.StringVar()

tk.geometry('420x450')

tk.title('Book Inventory App')

label1 = tkinter.Label(tk, text='Author First Name: ', font=labelfont, bg=bgcolor).grid(row=0, column=0, padx=labelpad)
entry1 = tkinter.Entry(tk, textvariable=name1).grid(row=0, column=1)
label2 = tkinter.Label(tk, text='Author Last Name: ', font=labelfont, bg=bgcolor).grid(row=1, column=0, padx=labelpad)
entry2 = tkinter.Entry(tk, textvariable=name2).grid(row=1, column=1)
label3 = tkinter.Label(tk, text='Book Title: ', font=labelfont, bg=bgcolor).grid(row=2, column=0, padx=labelpad)
entry3 = tkinter.Entry(tk, textvariable=title1).grid(row=2, column=1)
yearLabel = tkinter.Label(tk, text='Year Published: ', font=labelfont, bg=bgcolor).grid(row=3, column=0, padx=labelpad)
yearEntry = tkinter.Entry(tk, textvariable=year1).grid(row=3, column=1)
text1 = tkinter.Label(tk, text='Categories:', font=labelfont, bg=bgcolor).grid(row=4, column=1)
label4 = tkinter.Label(tk, text='Trees & Shrubs', bg=bgcolor, font=catfont).grid(row=5, column=0, padx=labelpad)
entry4 = tkinter.Radiobutton(tk, variable=cat1, value='ornamentals', bg=bgcolor).grid(row=5, column=1)
label5 = tkinter.Label(tk, text='Turf & Weeds', bg=bgcolor, font=catfont).grid(row=6, column=0, padx=labelpad)
entry5 = tkinter.Radiobutton(tk, variable=cat1, value='turf', bg=bgcolor).grid(row=6, column=1)
label6 = tkinter.Label(tk, text='Insects', bg=bgcolor, font=catfont).grid(row=7, column=0, padx=labelpad)
entry6 = tkinter.Radiobutton(tk, variable=cat1, value='insects', bg=bgcolor).grid(row=7, column=1)
label7 = tkinter.Label(tk, text='Fungus & Disease', bg=bgcolor, font=catfont).grid(row=8, column=0, padx=labelpad)
entry7 = tkinter.Radiobutton(tk, variable=cat1, value='disease', bg=bgcolor).grid(row=8, column=1)
label8 = tkinter.Label(tk, text='Plant Science', bg=bgcolor, font=catfont).grid(row=9, column=0, padx=labelpad)
entry8 = tkinter.Radiobutton(tk, variable=cat1, value='science', bg=bgcolor).grid(row=9, column=1)
label9 = tkinter.Label(tk, text='Golf & Sports', bg=bgcolor, font=catfont).grid(row=10, column=0, padx=labelpad)
entry9 = tkinter.Radiobutton(tk, variable=cat1, value='sports', bg=bgcolor).grid(row=10, column=1)
label10 = tkinter.Label(tk, text='General Landscape', bg=bgcolor, font=catfont).grid(row=10, column=0, padx=labelpad)
entry10 = tkinter.Radiobutton(tk, variable=cat1, value='general', bg=bgcolor).grid(row=10, column=1)
label11 = tkinter.Label(tk, text='Irrigation & Drainage', bg=bgcolor, font=catfont).grid(row=11, column=0, padx=labelpad)
entry11 = tkinter.Radiobutton(tk, variable=cat1, value='irrigation', bg=bgcolor).grid(row=11, column=1)
label12 = tkinter.Label(tk, text='Design', bg=bgcolor, font=catfont).grid(row=12, column=0, padx=labelpad)
entry12 = tkinter.Radiobutton(tk, variable=cat1, value='design', bg=bgcolor).grid(row=12, column=1)

# delete_label = tkinter.Label(tk, text='Book to Delete', font=labelfont, bg=bgcolor).grid(row=18, column=0, padx=labelpad)
# delete_entry = tkinter.Entry(tk, textvariable= deleteVar).grid(row=18, column=1)




def submit():

  thistitle = title1.get()
  firstName = name1.get()
  lastName = name2.get()
  if thistitle == "" or cat1.get() == "":
    tkinter.messagebox.showinfo('Error', 'No Title and/or Category Entered')
  else:
    if firstName == '' and lastName == '':
      print('Book entered is', thistitle)
    elif firstName == '':
      print('Book entered is', thistitle, 'authored by', lastName)
    elif lastName == '':
      print('Book entered is', thistitle, 'authored by', firstName)
    else:
      print('Book entered is', thistitle, 'authored by', firstName, lastName)
      
    conn = sqlite3.connect('newdb1', detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute(
      "INSERT INTO books (title, first_name, last_name, cat, year, input_date) VALUES (?, ? ,?, ?, ?, ?);",
      (thistitle, firstName, lastName, cat1.get(), year1.get(), datenow))
    conn.commit()
    conn.close()
    name1.set('')
    name2.set('')
    title1.set('')
    year1.set('')
    # cat1.set('')

def editBook():
  authName = tkinter.StringVar()
  authLastName = tkinter.StringVar()
  yearPub = tkinter.IntVar()
  authName.set('')
  authLastName.set('')

  
  newwindow = tkinter.Toplevel(tk)
  newwindow.title = 'Book Edit'
  newwindow.geometry('400x200')
  


  editTitle= tkinter.StringVar()
  titleLabel = tkinter.Label(newwindow, text='Book to Edit: ').grid(row=0, column=0)
  edit1 = tkinter.Entry(newwindow, textvariable= editTitle).grid(row=0, column =1)

  editlabel1 = tkinter.Label(newwindow, text='Author First Name: ', font=labelfont, bg=bgcolor).grid(row=1, column=0, padx=labelpad)
  editentry1 = tkinter.Entry(newwindow, textvariable=authName).grid(row=1, column=1)
  editlabel2 = tkinter.Label(newwindow, text='Author Last Name: ', font=labelfont, bg=bgcolor).grid(row=2, column=0, padx=labelpad)
  editentry2 = tkinter.Entry(newwindow, textvariable=authLastName).grid(row=2, column=1)
  edityearLabel = tkinter.Label(newwindow, text='Year Published: ', font=labelfont, bg=bgcolor).grid(row=3, column=0, padx=labelpad)
  edityearEntry = tkinter.Entry(newwindow, textvariable=yearPub).grid(row=3, column=1)

  editBtn = tkinter.Button(newwindow, command =lambda: editSingleRow(editTitle.get(), authName.get(), authLastName.get(), yearPub.get()), text='Submit').grid(row=4, column = 1)


def askQuestion():
  reply = tkinter.messagebox.askyesno(
    'confirmation', 'Are you sure you want delete ALL ROWS?')
  if reply == True:
    tkinter.messagebox.showinfo('Deleted', 'All Rows Deleted')
    deleteRows()
  else:
    tkinter.messagebox.showinfo('', 'Delete Canceled')




def deleteWindow():
  newwindow = tkinter.Toplevel(tk)
  newwindow.title = 'Delete Book'
  newwindow.geometry('325x200')

  
  deletewindow_label = tkinter.Label(newwindow, text='Book to Delete', font=labelfont, bg=bgcolor).grid(row=0, column=0, padx=labelpad, pady = 10)
  deletewindow_entry = tkinter.Entry(newwindow, textvariable= deletewindowtitle).grid(row=0, column=1)
  submit_delete = tkinter.Button(newwindow, command=askRow, text='DELETE BOOK', font=buttonFont, bg='red').grid(row=1, column = 1)
  close_window = tkinter.Button(newwindow, command=newwindow.destroy, text='CLOSE', font=buttonFont, bg='red').grid(row=1, column = 0)

def askRow():
  reply = tkinter.messagebox.askyesno('Delete Book', 'Delete Book From Database' )
  if reply == True:
    deleteRow(deletewindowtitle.get())
    tkinter.messagebox.showinfo('Deleted', 'Book Deleted')
  else:
    tkinter.messagebox.showinfo('', 'Delete Canceled')




btn1 = tkinter.Button(tk, command=submit, text='SUBMIT', font=buttonFont, bg=buttoncolor, fg='white').grid(row=13, column=1)
btn2 = tkinter.Button(tk, command=print_rows, text='PRINT CONSOLE', font=buttonFont, bg=buttoncolor, fg='white').grid(row=14, column=1)
btn3 = tkinter.Button(tk, command=panda_rows, text='PANDAS ROWS', font=buttonFont, bg=buttoncolor, fg='white').grid(row=15, column=1)
btn4 = tkinter.Button(tk, command=askQuestion, text='DELETE ALL BOOKS', font=buttonFont, bg='red').grid(row=16, column=0, padx=labelpad)
btn5 = tkinter.Button(tk, command=askExcel, text='TO EXCEL', font=buttonFont, bg=buttoncolor, fg='white').grid(row=16, column=1)
# btn6 = tkinter.Button(tk, command=askRow, text='DELETE BOOK', font=buttonFont, bg='red').grid(row=19, column = 1)
btn6 = tkinter.Button(tk, command=deleteWindow, text='DELETE BOOK', font=buttonFont, bg='red').grid(row=14, column = 0)
btn7 = tkinter.Button(tk, command=editBook, text='EDIT BOOK', font=buttonFont, bg='red').grid(row=15, column = 0)

tk.mainloop()

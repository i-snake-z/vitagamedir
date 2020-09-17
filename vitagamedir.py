#import sys
#sys.path.append(r'\vita_app\venv\Lib\site-packages')

import os
from xlrd import open_workbook
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv


list1 =[]

HEIGHT = 700
WIDTH = 900

root = tk.Tk()

root.title("Ps vita Directory games")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)



# frame = tk.Frame(root, bg='#80c1ff', bd=5)
# frame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.05)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.1)



entry0 = tk.Entry(frame, text= "Directory of games")
entry0.place(relx= 0.01, rely=0.01, relwidth=0.55, relheight=0.45)

entry1 = tk.Entry(frame, text= "Directory to extract")
entry1.place(relx= 0.01, rely=0.5, relwidth=0.55, relheight=0.45)





def browseFiles():
    filename = filedialog.askdirectory()
    entry0.delete(0, 'end')
    entry0.insert(0, filename)

def browseFilesextract():
    filename = filedialog.askdirectory()
    entry1.delete(0, 'end')
    entry1.insert(0, filename)

def clear():

    entry0.delete(0, 'end')
    entry1.delete(0, 'end')



def names():

    list1.clear()

    lower_frame = tk.Frame(root, bd=5, bg='#b3e7fd')
    lower_frame.place(relx=0.1, rely=0.15, relwidth=0.80, relheight=0.80)

    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)




    path = entry0.get()
    nameg = os.listdir(path)

    book = open_workbook('ultimate.xlsx')

    for x in nameg:
        for sheet in book.sheets():
            for rowidx in range(sheet.nrows):
                row = sheet.row(rowidx)
                for colidx, cell in enumerate(row):
                    if cell.value == x :
                        first_sheet = book.sheet_by_index(0)
                        cell = first_sheet.cell(rowidx, colidx)
                        cell1 = first_sheet.cell(rowidx,colidx + 1)

                        cell2 = str(cell)
                        cell3 = str(cell1)


                        cells = cell2.replace("text:","")
                        cells2 = cell3.replace("text:", "")

                        cellf1 = cells.replace("'", "")
                        cellf2 = cells2.replace("'", "")

                        list1.append([cellf1, cellf2])








    tempList = list1
    cols = ('ID_GAME', 'NAME OF GAME')
    listBox = ttk.Treeview(lower_frame, columns=cols, show='headings')




    for i, (name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(name, score))






    # set column headings
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    listBox.pack(fill='both',expand=1)


def extract():
    pathextract = entry1.get()

 

    fields = ['ID', 'GAME_ID']


    filename =  pathextract + "/export.csv"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(filename, 'w', newline='') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f, delimiter=';')

        write.writerow(fields)
        write.writerows(list1)






bt = tk.Button(frame, text = "Chose Directory of Games" ,command= browseFiles)
bt.place(relx= 0.57, rely=0.01, relwidth=0.30, relheight=0.45)

bt1 = tk.Button(frame, text = "GO" ,command= names)
bt1.place(relx=0.88, rely=0.01, relwidth=0.05, relheight=0.45)

bt2 = tk.Button(frame, text = "Chose Directory to Extract CSV" ,command= browseFilesextract)
bt2.place(relx= 0.57, rely=0.5, relwidth=0.30, relheight=0.45)

bt3 = tk.Button(frame, text = "GO" ,command= extract)
bt3.place(relx=0.88, rely=0.5, relwidth=0.05, relheight=0.45)

bt4 = tk.Button(frame, text = "CLEAR" ,command= clear)
bt4.place(relx=0.94, rely=0.01, relwidth=0.06, relheight=0.95)




root.mainloop()
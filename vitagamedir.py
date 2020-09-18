#import sys
#sys.path.append(r'\vita_app\venv\Lib\site-packages')

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import csv

#Settings
WINDOW_NAME     = "vitagamedir"
WINDOW_HEIGHT   = 700
WINDOW_WIDTH    = 900

#Tk window setup
root = tk.Tk()
root.title(WINDOW_NAME)
canvas = tk.Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()
background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.1)

#Buttons setup
game_directory_entry = tk.Entry(frame, text= "Path to games")
game_directory_entry.place(relx= 0.01, rely=0.01, relwidth=0.55, relheight=0.45)
extract_directory_entry = tk.Entry(frame, text= "Directory to extract")
extract_directory_entry.place(relx= 0.01, rely=0.5, relwidth=0.55, relheight=0.45)

#Globals
current_dir_games = []

class db_entry:
    code = ""
    name = ""

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __eq__(self, other):
        return self.code == other

db_cache = []

with open("./db.csv", "r", encoding="UTF-8") as db_file:
    #print("reading db.csv...")
    csv_reader = csv.reader(db_file, delimiter=",")
    for row in csv_reader:
        gameinfile = db_entry(row[0], row[1])
        db_cache.append(gameinfile)
    #print("done, found {} entries".format(len(db_cache)))




def browseFiles():
    filename = filedialog.askdirectory()
    game_directory_entry.delete(0, 'end')
    game_directory_entry.insert(0, filename)

def browseFilesextract():
    filename = filedialog.askdirectory()
    extract_directory_entry.delete(0, 'end')
    extract_directory_entry.insert(0, filename)




def names():
    current_dir_games.clear()
    path = game_directory_entry.get()

    if path == "":
        messagebox.showinfo("Info", "Please insert path of the games")

    else:
        lower_frame = tk.Frame(root, bd=5, bg='#b3e7fd')
        lower_frame.place(relx=0.1, rely=0.15, relwidth=0.80, relheight=0.80)

        def clear():
            game_directory_entry.delete(0, 'end')
            extract_directory_entry.delete(0, 'end')
            lower_frame.destroy()

        bt_clear = tk.Button(frame, text="CLEAR", command=clear)
        bt_clear.place(relx=0.94, rely=0.01, relwidth=0.06, relheight=0.95)

        # path = game_directory_entry.get()
        directory_list = os.listdir(path)

        for directory in directory_list:
            for game in db_cache:
                if game == directory:
                    # print("Found {}".format(directory))
                    current_dir_games.append([game.code, game.name])

        tempList = current_dir_games
        cols = ('ID_GAME', 'NAME OF GAME')
        listBox = ttk.Treeview(lower_frame, columns=cols, show='headings')

        for i, (name, score) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(name, score))

        # set column headings
        for col in cols:
            listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)

        listBox.pack(fill='both', expand=1)


def extract():
    pathextract = extract_directory_entry.get()

    if pathextract == "":
        messagebox.showinfo("Info", "Please insert path to extract")

    else:
        fields = ['ID', 'GAME_ID']

        filename = pathextract + "/export.csv"
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(filename, 'w', newline='') as f:

            # using csv.writer method from CSV package
            write = csv.writer(f, delimiter=';')

            write.writerow(fields)
            write.writerows(current_dir_games)

        messagebox.showinfo("Info", "Extract Complete")

def snake_():
    messagebox.showinfo("Enjoy", "Hope you like this app :)")



bt_browse_game_folder = tk.Button(frame, text = "Chose Directory of Games" ,command= browseFiles)
bt_browse_game_folder.place(relx= 0.57, rely=0.01, relwidth=0.30, relheight=0.45)

bt_go_dir_games = tk.Button(frame, text = "GO" ,command= names)
bt_go_dir_games.place(relx=0.88, rely=0.01, relwidth=0.05, relheight=0.45)

bt_browse_extract_folder = tk.Button(frame, text = "Chose Directory to Extract CSV" ,command= browseFilesextract)
bt_browse_extract_folder.place(relx= 0.57, rely=0.5, relwidth=0.30, relheight=0.45)

bt_go_dir_extract = tk.Button(frame, text = "GO" ,command= extract)
bt_go_dir_extract.place(relx=0.88, rely=0.5, relwidth=0.05, relheight=0.45)


snake = tk.Button(root, text = "i-snake-z",command= snake_)
snake.place(relx=0.93, rely=0.955, relwidth=0.06, relheight=0.03)



root.mainloop()

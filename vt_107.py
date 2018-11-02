#py3.7
version = "1.07"
from tkinter import *
import csv
import random
import sys

#pulls out random word from vocabulary csv
z = random.randint(1,50)

with open('vocs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    delist = []
    enlist = []
    for row in readCSV:
        eng = row[1]
        deu = row[0]

        delist.append(deu)
        enlist.append(eng)

#tkinter
def show_entry_fields():
    txt.delete(0.0, 'end')
    txtName = wordde.get()
    if wordde.get() == enlist[z]:
        antwort = "Correct."
    else:
        antwort = "Wrong. It's " +"'" +enlist[z]  +"'"

    sentence = antwort
    txt.insert(0.0, sentence)    
master = Tk()
master.geometry("300x100")

master.title("Vokabeltrainer " +version)

Label(master, text="English-German").grid(row=0)
Label(master, text='"'+delist[z]+'"'+ ' in german is: ').grid(row=1)

wordde = Entry(master)

wordde.grid(row=1, column=1)

btn2 = Button(master, text='Check', command=show_entry_fields)
btn2.grid(row=3, column=1, sticky=W, pady=4)
txt = Text(master, width=35, height=1, wrap=WORD)
txt.grid(row=4, columnspan=2, sticky=W)

mainloop( )

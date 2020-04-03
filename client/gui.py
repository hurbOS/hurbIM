import tkinter as tk
from tkinter import *

def send(event):
    thing=entry.get()
    file = open(r'message.txt','w')
    file.write(thing)
    file.close()
    entry.delete (0, last=len(thing))

window = tk.Tk()
window.title("hurbIM")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=610, weight=1)

fr1 = tk.Frame(window, relief=tk.RAISED, bd=2)
fr2 = tk.Frame(window, relief=tk.RAISED, bd=2)
fr3 = tk.Frame(window, relief=tk.RAISED, bd=2)
convos = tk.Listbox(fr1, width=30,height=37)
chat = tk.Listbox(fr2, width=100, height=36)
entry = tk.Entry(fr2, width=70,)
entry.bind('<Return>', send)
var = StringVar()
convosTitle = tk.Label(fr1, textvariable=var, relief=RAISED, width=30)
var.set("Messages")

convosTitle.grid(row=0, column=0, sticky="n")
convos.grid(row=1, column=0, sticky="ew")
fr1.grid(row=0, column=0, sticky="ew")
fr2.grid(row=0, column=1, sticky="ew")
fr3.grid(row=0, column=2, sticky="ns")
entry.grid(row=1, column=1, sticky="ew")
chat.grid(row=0,column=1,sticky="nsew")
convos.grid(row=0,column=0,sticky="ns")

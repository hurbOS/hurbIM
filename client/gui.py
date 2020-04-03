import tkinter as tk
from tkinter import *
from cryption import *
import os

def send(event):
    thing=entry.get()
    file = open('message.txt','x')
    file.write(thing)
    file.close()
    entry.delete (0, last=len(thing))
    write_key()
    key = load_key()
    file = "message.txt"
    encrypt(file, key)

window = tk.Tk()
window.title("hurbIM")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=610, weight=1)
window.configure(bg="#101116")
fr1 = tk.Frame(window, relief=tk.RAISED, bd=2)
fr2 = tk.Frame(window, relief=tk.RAISED, bd=2)
convos = tk.Listbox(fr1, width=30,height=37)
convos.insert(1, "Python")
convos.insert(2, "Perl")
convos.insert(3, "C")
convos.insert(4, "PHP")
convos.insert(5, "JSP")
convos.insert(6, "Ruby")
chat = tk.Text(fr2, width=100, height=38)
entry = tk.Entry(fr2, width=70,)
entry.bind('<Return>', send)
var = StringVar()
convosTitle = tk.Label(fr1, textvariable=var, relief=RAISED, width=30)
var.set("Messages")

convosTitle.grid(row=0, column=0, sticky="n")
convos.grid(row=1, column=0, sticky="ew")
fr1.grid(row=0, column=0, sticky="ns")
fr2.grid(row=0, column=1, sticky="ns")
entry.grid(row=1, column=1, sticky="ew")
chat.grid(row=0,column=1,sticky="nsew")
convos.grid(row=0,column=0,sticky="ns")

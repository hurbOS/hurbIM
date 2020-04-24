import curses
import npyscreen
import sqlite3
import datetime
import time
import settings

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from encryption import *
from database import *
from contactbase import *


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

class InputBox(npyscreen.MultiLineEdit):
    def __init__(self, *args, **keywords):
        super(InputBox, self).__init__(*args, **keywords)
        self.add_handlers({
            curses.ascii.NL: self.when_add_Message,
        })

    def when_add_Message(self, *args, **keywords):
        try:
            wgsender = "UserName"
            wgreciever = settings.message_sender
            self.wgcontents  = self.value
            wgtimestamp = datetime.datetime.now()

            self.parent.parentApp.myDatabase.add_record(
            sender = wgsender,
            reciever = wgreciever,
            contents = self.wgcontents,
            timestamp = wgtimestamp,
            )

            self.value = ""
            messages = self.parent.parentApp.myDatabase.get_record(wgreciever)
            self.parent.update_message_list(messages)
        except:
            self.value = ""

class BoxTitle(npyscreen.BoxTitle):
     _contained_widget = InputBox

class RecordListDisplay(npyscreen.FormBaseNew):
    def create(self):
        self.name="HurbIM"
        y, x = self.useable_space()
        self.ChatBox = self.add(BoxTitle2, name="Chats", relx=2, max_width=x // 6 +4, rely=1,
                                   max_height=0,values=[])
        self.MessageBox = self.add(BoxTitle3,name="Messages", rely=1, relx=(x // 5) + 1, max_height=-3,
                                      custom_highlighting=True, highlighting_arr_color_data=[0],values=[
                                      "██╗  ██╗██╗   ██╗██████╗ ██████╗     ██╗███╗   ███╗",\
                                      "██║  ██║██║   ██║██╔══██╗██╔══██╗    ██║████╗ ████║",\
                                      "███████║██║   ██║██████╔╝██████╔╝    ██║██╔████╔██║",\
                                      "██╔══██║██║   ██║██╔══██╗██╔══██╗    ██║██║╚██╔╝██║",\
                                      "██║  ██║╚██████╔╝██║  ██║██████╔╝    ██║██║ ╚═╝ ██║",\
                                      "╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝╚═╝     ╚═╝",\
                                      "- Welcome to hurbIM, a free, open source messenger alternative.",\
                                      "- To add a contact, type 'ctrl + a' while selecting the right hand bar", \
                                      "- To select a contact, select it with enter from the right menu", \
                                      "- For further help hit '?' to see a list of commands"])
        self.InputBox = self.add(BoxTitle, name="Input", relx=(x // 5) + 1, rely=-5,max_height=-3)

    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        self.ChatBox.values = self.parentApp.myDatabase2.list_all_records()
        self.ChatBox.display()

    def update_message_list(self, messagelist):
        self.MessageBox.values = messagelist
        self.MessageBox.display()

class gui(npyscreen.NPSAppManaged):
    def onStart(self):
        self.myDatabase = MessageDatabase()
        self.myDatabase2 = AddressDatabase()
        self.addForm("MAIN", RecordListDisplay)
        self.addForm("EDITRECORDFM", EditContact)

if __name__ == '__main__':
    HOST = 'hurbindustries.net'
    PORT = 33000

    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    receive_thread = Thread(target=receive)
    receive_thread.start()
    myApp = gui()
    myApp.run()

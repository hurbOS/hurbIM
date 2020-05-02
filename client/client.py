import curses
import npyscreen
import time
import settings
import auth

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from encryption import *
from contactbase import *
from database import *
from tui import *

def receive():
    text_read = open('temp', 'w')
    while True:
            msg = client_socket.recv(BUFSIZ)
            if not msg:
                break
            dec = msg.decode("utf-8")
            for item in dec:
                item.split(',')
            text_read.write(str(dec))

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
                                      "- For further help hit '?' to see a list of commands"\
                                      ]
)
        self.InputBox = self.add(BoxTitle, name="Input", relx=(x // 5) + 1, rely=-5,max_height=-3)

    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        self.ChatBox.values = self.parentApp.myDatabase2.list_all_records()
        self.ChatBox.display()

    def update_message_list(self, messagelist):
        self.MessageBox.values = messagelist
        self.MessageBox.display()

    def sendmsg(self, contents):
        client_socket.send(contents)

class gui(npyscreen.NPSAppManaged):
    def onStart(self):
        self.myDatabase = MessageDatabase()
        self.myDatabase2 = AddressDatabase()
        self.addForm("MAIN", RecordListDisplay)
        self.addForm("EDITRECORDFM", EditContact)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 6901
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    global client_socket
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)
    auth.authenticate(client_socket)
    receive_thread = Thread(target=receive)
    receive_thread.start()
    myApp = gui()
    myApp.run()

import npyscreen
import time
import settings
import auth
import database

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from contactbase import *
from tui import *

def receive():
    text_read = open('temp', 'w')
    while True:
            msg = client_socket.recv(BUFSIZ)
            if not msg:
                break
            dec = msg.decode("utf-8")
            l = dec.replace('(', '')
            p = l.replace(')', '')
            k = p.replace(',', '')
            q = k.split("'")
            for i in range(3):
                q.pop(i)
            database.MessageDatabase.add_record(sender=q[0],receiver=q[1],contents=q[2],timestamp=time.ctime())

class RecordListDisplay(npyscreen.FormBaseNew):
    def create(self):
        self.name="HurbIM"
        y, x = self.useable_space()
        self.ChatBox = self.add(BoxTitle2, name="Chats", relx=2, max_width=x // 6 +4, rely=1,
                                   max_height=0,values=[])
        self.MessageBox = self.add(BoxTitle3,name="Messages", rely=1, relx=(x // 5) + 1, max_height=-3,
                                      custom_highlighting=True, highlighting_arr_color_data=[0],values=[
                                       " _   _ _   _ ____  ____    ___ __  __",\
                                       "| | | | | | |  _ \| __ )  |_ _|  \/  |",\
                                       "| |_| | | | | |_) |  _ \   | || |\/| |",\
                                       "|  _  | |_| |  _ <| |_) |  | || |  | |",\
                                       "|_| |_|\___/|_| \_\____/  |___|_|  |_|",\
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
        self.myDatabase = database.MessageDatabase()
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

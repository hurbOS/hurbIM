import curses
import npyscreen
import sqlite3
import datetime
import time
import settings

from cryption import *
from database import *
from contactbase import *


class InputBox(npyscreen.MultiLineEdit):
    def __init__(self, *args, **keywords):
        super(InputBox, self).__init__(*args, **keywords)
        self.add_handlers({
            curses.ascii.NL: self.when_add_Message,
        })

    def when_add_Message(self, *args, **keywords):
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

class RecordListDisplay(npyscreen.Form):
    def create(self):
        y, x = self.useable_space()
        self.ChatBox = self.add(RecordList, name="Chats", relx=2, max_width=x // 6, rely=1,
                                   max_height=0,values=[])
        self.MessageBox = self.add(MessageRecordList,name="Messages", rely=1, relx=(x // 5) + 1, max_height=-3,
                                      custom_highlighting=True, highlighting_arr_color_data=[0],values=[])
        self.InputBox = self.add(InputBox, name="Input", relx=(x // 5) + 1, rely=-5,max_height=-3)

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
    myApp = gui()
    myApp.run()

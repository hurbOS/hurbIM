import curses
from cryption import *
import npyscreen
import sqlite3
import time
from database import *
from contactbase import *

class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class RecordListDisplay(npyscreen.Form):
    def create(self):
        #self.add_handlers({
        #    curses.ascii.NL:()
        #})
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
        self.addForm("EDITMESSAGE", EditMessage)

if __name__ == '__main__':
    myApp = gui()
    myApp.run()

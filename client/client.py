import curses
from cryption import *
import npyscreen
import sqlite3
import time
from database import *

class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class RecordListDisplay(npyscreen.Form):
    def create(self):

        y, x = self.useable_space()
        self.ChatBox = self.add(RecordList, name="Chats", relx=2, max_width=x // 6, rely=1,
                                   max_height=0,values=[])
        self.MessageBox = self.add(MessageRecordList,name="Messages", rely=1, relx=(x // 5) + 1, max_height=-3,
                                      custom_highlighting=True, highlighting_arr_color_data=[0])
        self.InputBox = self.add(InputBox, name="Input", relx=(x // 5) + 1, rely=-5,max_height=-3)

    def inputbox_submit(self, _input):
        z = str(self.InputBox.value)
        self.update_list()
        self.InputBox.value = ""
        self.InputBox.display()

    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        self.MessageBox.display()
        self.ChatBox.values = self.parentApp.myDatabase.list_all_records()
        self.ChatBox.display()

class gui(npyscreen.NPSAppManaged):
    def onStart(self):
        self.myDatabase = MessageDatabase()
        self.addForm("MAIN", RecordListDisplay)
        self.addForm("EDITMESSAGE", EditMessage)

if __name__ == '__main__':
    myApp = gui()
    myApp.run()

import npyscreen
from cryption import *
# This application class serves as a wrapper for the initialization of curses
# and also manages the actual forms of the application

m = open("/home/wilson/Documents/Code/hurbIM/client/welcome.txt","r").readlines()
n = open("/home/wilson/Documents/Code/hurbIM/client/messagein.txt","r").readlines()
o = open("/home/wilson/Documents/Code/hurbIM/client/messageout.txt","w")
openFile=m
numLines=sum(1 for line in openFile)

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm(name="HurbIM"))

class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit
class MessageBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.Pager

class MainForm(npyscreen.Form):
    def create(self):
        y, x = self.useable_space()
        self.add(MessageBox, name="Chats", value=0, relx=1, max_width=x // 5, rely=1,
                                   max_height=0,values=[])

        self.add(MessageBox,name="Messages", rely=1, relx=(x // 5) + 1, max_height=-3, editable=True,
                                      custom_highlighting=True, highlighting_arr_color_data=[0],values=[openFile])

        self.add(InputBox, name="Input", relx=(x // 5) + 1, rely=-5,max_height=-3)
    def afterEditing(self):
        self.parentApp.setNextForm(None)

if __name__ == '__main__':
    TA = MyTestApp()
    TA.run()

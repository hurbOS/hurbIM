import npyscreen
import random

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Hello Medium!")

class InputBox(npyscreen.BoxTitle):
    # MultiLineEdit now will be surrounded by boxing
    _contained_widget = npyscreen.MultiLineEdit

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        y, x = self.useable_space()
        obj = self.add(npyscreen.BoxTitle, name="BoxTitle",
              custom_highlighting=True, values=["first line", "second line"],
              rely=y // 4, max_width=x // 2 - 5, max_height=y // 2)
        self.add(InputBox, name="Boxed MultiLineEdit", footer="footer",
              relx=x // 2, rely=2)
MyApp = App()
MyApp.run()

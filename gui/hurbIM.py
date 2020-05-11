import kivy
from kivy.config import Config
from kivy.app import App, Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty

Config.set("input","mouse", "mouse, multitouch_on_demand")

class LoginPage(Screen):
    user = ObjectProperty(None)
    passw = ObjectProperty(None)

    def createAcc(self):
        sm.current = "CreateAccount"

    def login(self):
        sm.current = "ChatPage"

class CreateAccount(Screen):
    # Username, Password and ConfirmPassword
    u = ObjectProperty(None)
    p = ObjectProperty(None)
    cp = ObjectProperty(None)

    def createAcc(self):
        usernm = str(self.u.text).strip(" ")
        passw = str(self.p.text).strip(" ") 
        confPass = str(self.cp.text).strip(" ")

        print(usernm, passw, confPass)      

class ChatPage(Screen):
    pass 

class WindowManager(ScreenManager):
    pass


config = Builder.load_file("config.kv")
sm = WindowManager()
screens = [LoginPage(name="LoginPage"),
        CreateAccount(name="CreateAccount"),
        ChatPage(name="ChatPage")]

for screen in screens:
    sm.add_widget(screen)

class MainApp(App):
    def build(self):
        self.title = "hurbIM"
        return sm

if __name__ == "__main__":
    mainApp = MainApp() 
    mainApp.run()




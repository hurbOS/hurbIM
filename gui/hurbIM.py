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
        if user.text == "admin" and pass.text == "admin":
            sm.current = "ChatPage"
        else: 
            pass
class CreateAccount(Screen):
    pass

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




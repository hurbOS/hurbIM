import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock

kivy.require("1.11.1")
Config.set("input","mouse", "mouse, multitouch_on_demand")
Clock.max_iteration = 1

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class LoginPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (90, 120)

        self.box = BoxLayout(
            orientation = "vertical",
            padding = [20, 20]

        )
        self.logo = Image(
            source = "logo_white.png",
            size_hint = (1, 0.5),
        )

        self.username = TextInput(
            hint_text = "Username", 
            multiline = False, 
            size_hint = (0.5, None), 
            height = 38,
            pos_hint = {
                    "top": 0.50,
                    "bottom" : 0.65,
                    "x": 0.25

                }
        )
        self.password = TextInput(
            hint_text = "Password", 
            multiline =False, 
            size_hint =(0.5, None), 
            height = 38, 
            pos_hint = {
                    "x": 0.25,
                    "y": 0.35
            }
        )
        self.btn = Button(
            text = "Login",
            font_name = "RobotoConReg.ttf",
            font_size = 18,
            size_hint = (0.45, None),
            height = 50,
            pos_hint = {
                    "x": 0.28,
                    "y": 0.2,
                    "top": 0.26
            }
        )

        self.prompt = Label(
            text = "Create Account",
            size_hint = (0.1, None),
            height = 10,
            underline = True,
            color = (72, 133, 237, 1),
            pos_hint = {
                    "x": 0.3,
                    "y": 0.7,
                    "top": 0.3
            }
        )
        self.create = Label(
            text = "Create Account",
            size_hint = (0.1, None),
            height = 10,
            pos_hint = {
                    "x": 0.45,
                    "y": 0.3,
                    "top": 0.32
            }
        )
        self.box.add_widget(self.logo)
        self.box.add_widget(Label(text=""))
        self.add_widget(self.box)
        self.add_widget(self.username) 
        self.add_widget(self.password)
        self.add_widget(self.btn)
        self.add_widget(self.create)
             

class CreateAccount(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ChatPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(App):
    def build(self):
        
        self.screen_manager = ScreenManager()
        self.title = "hurbIM"

        self.LoginPage = LoginPage()
        screen = Screen(name="Login Page")
        screen.add_widget(self.LoginPage)
        self.screen_manager.add_widget(screen)

        self.CreateAccount = CreateAccount()
        screen = Screen(name="CreateAccount")
        screen.add_widget(self.CreateAccount)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.run()




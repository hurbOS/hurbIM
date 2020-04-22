import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

kivy.require("1.11.1")
Config.set("input","mouse", "mouse, multitouch_on_demand")

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

        self.logo = Image(
            source="logo_white.png",
            padding=[10, 10, 10, 10],
            
        )

        self.username = TextInput(
            hint_text="Username", 
            multiline=False, 
            size_hint=(0.4, None), 
            height=30,
            pos_hint={
                    "top": 1
                }
        )
        self.password = TextInput(
            hint_text = "Password", 
            multiline=False, 
            size_hint=(0.4, None), 
            height=30, 
            pos_hint={
                    "top": 0.25,
                    "x": 0.5
            }
        )
        self.btn = Button(
            text="Login", 
            size_hint=(0.3, 0.2),
            pos_hint={
                    "top": 0.1
            }
        )

        self.add_widget(self.logo)
        self.add_widget(self.username) 
        self.add_widget(self.password)
        self.add_widget(self.btn)
             

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




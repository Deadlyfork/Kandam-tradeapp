from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons

class SearchPage(MDScreen):
    pass

class HomePage(MDScreen):
    pass

class RegisterPage(MDScreen):
    pass

class LoginPage(MDScreen):
    pass

class ScreenManagement(ScreenManager):
    pass

class Kandam(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file("kandam_builder.kv")

if __name__ == '__main__':
    Kandam().run()
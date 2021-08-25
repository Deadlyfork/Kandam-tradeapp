from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
'''
class SearchPage(MDScreen):
    pass

class NewTradePage(MDScreen):
    pass

class MyTradesPage(MDScreen):
    pass

class HomePage(MDScreen):
    pass

class RegisterPage(MDScreen):
    pass
'''
class LoginPage(MDScreen):
    pass

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('kandam_builder.kv')

class Kandam(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" 
        return kv_file

if __name__ == '__main__':
    Kandam().run()

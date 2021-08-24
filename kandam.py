from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file('kandam.kv')


class Kandam(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" 

if __name__ == '__main__':
    Kandam().run()

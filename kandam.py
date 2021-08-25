
from kivy.lang import Builder

from kivymd.app import MDApp

#kv_file = Builder.load_file("kandam_builder.kv")

class Kandam(MDApp):
    def build(self):
        return Builder.load_file("kandam_builder.kv")

if __name__ == '__main__':
    Kandam().run()
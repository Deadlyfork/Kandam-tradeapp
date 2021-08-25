from kivymd.app import MDApp
from kivy.lang import Builder


kv_file = Builder.load_file("kandam_builder.kv")

class Kandam(MDApp):
    def build(self):
        return kv_file

if __name__ == '__main__':
    Kandam().run()
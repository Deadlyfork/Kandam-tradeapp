from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
import data_sql

class NewTradePage(MDScreen):
    pass

class SearchPage(MDScreen):
    
    def set_list_items(self, text="", search=False):

        def add_item(name_item):
            self.ids.rv.data.append(
                {
                    "viewclass": 'OneLineListItem',
                    "text": name_item
                }
            )



        self.ids.rv.data = []

        items_names = list(data_sql.items_names())

        for name_item in items_names:
            if search:
                if text in name_item:
                    add_item(name_item)
            else:
                add_item(name_item)


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
        self.theme_cls.primary_palette = 'Pink'
        return Builder.load_file("kandam_builder.kv")


if __name__ == '__main__':
    Kandam().run()
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
import data_sql

class NewOfferPage(MDScreen,):
    pass

class SearchPage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)





'''
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
'''

class HomePage(MDScreen):
    pass

class RegisterPage(MDScreen):
    def register(self):
        username = self.ids.uname.text  
        gamename = self.ids.gname.text  
        useremail = self.ids.email.text
        password = self.ids.upass.text

        data_sql.register(username,gamename,useremail,password)

class LoginPage(MDScreen):
    def verify_pass(self):
        loginuname = str(self.ids.unamelogin.text)
        loginpass = str(self.ids.passlogin.text)

        password = ''.join(data_sql.password(loginuname))

        try:
            if password==loginpass:
                self.manager.current = 'home'
        except:
            self.manager.current = 'login'

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Kandam(MDApp):
    def build(self):
        ScreenManagement().add_widget(SearchPage(name='menu'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Indigo'
        return Builder.load_file("kandam_builder.kv")


if __name__ == '__main__':
    Kandam().run()
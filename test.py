from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp





class Var(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical')
        label = MDLabel()
        label1 = MDToolbar(title='Woor')

        layout.add_widget(label1)
        layout.add_widget(label)
        self.add_widget(layout)



class Kandam(MDApp):
    def build(self):
        
        self.screen_manager = ScreenManager()
        
        self.var = Var()
        

        screen = MDScreen()
        screen.add_widget(self.var)
        self.screen_manager.add_widget(screen)


        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Indigo'

        return self.screen_manager




if __name__ == '__main__':
    Kandam().run()

















'''

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window

class Menu(GridLayout):
    #Screen 3
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 2

        self.search_input = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.search_button = Button(text='Search')
        self.search_button.bind(on_press=self.search_offers)

        self.home_page = Label(height=Window.size[1]*0.9, size_hint_y=None)
        
        top_line = GridLayout(cols=2)
        top_line.add_widget(self.search_input)
        top_line.add_widget(self.search_button)
        self.add_widget(top_line)
        self.add_widget(self.home_page)

    def search_offers(self, _): 
        #hannan
        pass

class InfoPage(GridLayout):
    # SCREEN 2
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        
        self.message = Label(halign='center', valign= 'middle', font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        #For the message not to go beyond the window
        self.message.text_size = (self.message.width*0.9, None)

class LoginScreen(GridLayout):
    # LOGIN SCREEN / SCREEN 1
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        #Inputing name

        self.add_widget(Label(text='Name'))
        self.name = TextInput(multiline= False)
        self.add_widget(self.name) 
        
        #Inputing email 
        self.add_widget(Label(text='Email'))
        self.email = TextInput(multiline= False)
        self.add_widget(self.email)
        
        #Inputing password
        self.add_widget(Label(text= 'Password'))
        self.password = TextInput(multiline= False)
        self.add_widget(self.password)
        
        #Building a submit button
        self.submit = Button(text='Submit')
        self.submit.bind(on_press=self.submit_button)
        self.add_widget(self.submit)

    def submit_button(self, _):
        #After submition
        name = self.name.text
        email = self.email.text
        password = self.password.text
        info = ';)' 
        trade_app.info_page.update_info(info)       
        trade_app.screen_manager.current = 'info'
        Clock.schedule_once(self.change_screen, 1)
    def change_screen(self, _):
        trade_app.screen_manager.current = 'menu'
class kandam(App):
    # BASE CLASS
    def build(self):
        #Building a window to display 
        self.screen_manager = ScreenManager()
        self.login_screen = LoginScreen()
        
        #Building screen 1 - Login screen
        screen = Screen()
        screen.add_widget(self.login_screen)
        self.screen_manager.add_widget(screen)
        
        #Building screen 2 - information page
        self.info_page = InfoPage()
        screen = Screen(name='info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        #Building screen 3 - Menu
        self.menu = Menu()
        screen = Screen(name ='menu')
        screen.add_widget(self.menu)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == '__main__':
    trade_app = kandam()
    trade_app.run()


<SearchPage>
    
    name: 'search'

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDBoxLayout:
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search'
                on_text: root.set_list_items(self.text, True)

            MDFillRoundFlatButton:
                text:'Back'
                pos_hint:{"x":0.5,'y':0.3}
                on_press: app.root.current = 'home'

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'
            
            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'

'''
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class Menu(GridLayout):
    #Screen 3
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        

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

        #Inputting name 
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

    def submit_button(self, instance):
        #After submition
        name = self.name.text
        email = self.email.text
        password = self.password.text
        info = ';)' 
        trade_app.info_page.update_info(info)       
        trade_app.screen_manager.current = 'info'

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
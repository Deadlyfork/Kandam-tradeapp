import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(GridLayout):
    # LOGIN SCREEN
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
       
        self.add_widget(Label(text='Name'))
        self.Name = TextInput(multiline= False)
        self.add_widget(self.Name) 

        self.add_widget(Label(text='Email'))
        self.email = TextInput(multiline= False)
        self.add_widget(self.email)
        
        self.add_widget(Label(text= 'Password'))
        self.password = TextInput(multiline= False)
        self.add_widget(self.password)
        
        self.submit = Button(text='Submit')
        self.add_widget(self.submit)

    def submit_button(self):
        email = self.email.text
        password = self.password.text        

class kandam(App):
    # BASE CLASS
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    kandam().run()
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


class SellScreen(GridLayout): #need to add - text input, label 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.submit_trade = Button(text='Submit Trade')
        self.add_widget(self.submit_trade)
        self.submit_trade.bind(on_press=self.submit_trade_pressed)

    def submit_trade_pressed(self, _):
        trade_app.screen_manager.current = 'menu'

class BuyScreen(GridLayout):  #need to add - text input, label  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.submit_trade = Button(text='Submit Trade')
        self.add_widget(self.submit_trade)
        self.submit_trade.bind(on_press=self.submit_trade_pressed)

    def submit_trade_pressed(self, _):
        trade_app.screen_manager.current = 'menu'

class WoodScreen(GridLayout):
    #Items screen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.sell_button = Button(text='SELL')
        self.add_widget(self.sell_button)
        self.sell_button.bind(on_press=self.sell_pressed)

        self.buy_button = Button(text='BUY')
        self.add_widget(self.buy_button)
        self.buy_button.bind(on_press=self.buy_pressed)

    def sell_pressed(self, _):
        trade_app.screen_manager.current = 'sell'
    
    def buy_pressed(self, _):
        trade_app.screen_manager.current = 'buy'

class MenuScreen(GridLayout):
    #Screen 3
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 3

        self.my_offers = Button(text='My Offers') 

        self.search_input = TextInput(height=Window.size[1]*0.1, width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.search_button = Button(text='Search')
        self.search_button.bind(on_press=self.all_items_search)

        self.home_page = Label(height=Window.size[1]*0.8, size_hint_y=None)
        
        searchbar_line = GridLayout(cols=2)
        searchbar_line.add_widget(self.search_input)
        searchbar_line.add_widget(self.search_button)
        self.add_widget(searchbar_line)
        self.add_widget(self.home_page)

    def all_items_search(self, _): 
        search_phrase = str(self.search_input.text.lower())

        try:
            trade_app.screen_manager.current = search_phrase
        except:
            trade_app.screen_manager.current = 'menu'
        
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
        self.screen_manager = ScreenManager()
        self.login_screen = LoginScreen()
        
        #Building screen 1 - Login screen
        screen = Screen(name='login')
        screen.add_widget(self.login_screen)
        self.screen_manager.add_widget(screen)
        
        #Building screen 2 - information page
        self.info_page = InfoPage()
        screen = Screen(name='info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        #Building screen 3 - Menu
        self.menu_screen = MenuScreen()
        screen = Screen(name ='menu')
        screen.add_widget(self.menu_screen)
        self.screen_manager.add_widget(screen)

        #item screen 1 - wood
        self.wood_screen = WoodScreen()
        screen = Screen(name='wood')
        screen.add_widget(self.wood_screen)
        self.screen_manager.add_widget(screen)

        #Buy screen
        self.buy_screen = BuyScreen()
        screen = Screen(name='buy')
        screen.add_widget(self.buy_screen)
        self.screen_manager.add_widget(screen)

        #Sell screen
        self.sell_screen = SellScreen()
        screen = Screen(name='sell')
        screen.add_widget(self.sell_screen)
        self.screen_manager.add_widget(screen)


        return self.screen_manager

if __name__ == '__main__':
    trade_app = kandam()
    trade_app.run()




'''
TODO
----
insert custom price

work on sell, buy screen - add text input and label

work on item screen - add an empty label to beutify 

add one more item screen - stone

back button for item screen

back button to my offers page - add updatability, add deletion method

adding set offers to a table in database

adding set offers to my offers page1

scrollability to my offers page
'''
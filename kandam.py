import kivy
kivy.require('2.0.0')

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window

class LoginScreen(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.login = MDLabel(text="Hello, World", halign="center")
        self.add_widget(self.login)

class kandam(MDApp):
    # BASE CLASS
    def build(self):
        #Building a window to display 
        self.screen_manager = ScreenManager()

        self.theme_cls.bg_light 
        self.theme_cls.theme_style = "Dark"

        #Building screen 1 - Login screen
        self.login_screen = LoginScreen()
        screen = Screen()
        screen.add_widget(self.login_screen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == '__main__':
    trade_app = kandam()
    trade_app.run()

'''
class OfferScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.submit_trade = Button(text='Submit Trade')
        self.add_widget(self.submit_trade)
        self.submit_trade.bind(on_press=self.submit_trade_pressed)

    def submit_trade_pressed(self, _):
        trade_app.screen_manager.current = 'menu'

class ItemScreen(GridLayout):
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
        trade_app.screen_manager.current = 'offer'
    
    def buy_pressed(self, _):
        trade_app.screen_manager.current = 'offer'

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
        search_phrase = self.search_input.text.lower()
        
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

        #items screen
        self.items_screen = ItemScreen()
        screen = Screen(name='items')
        screen.add_widget(self.items_screen)
        self.screen_manager.add_widget(screen)

        #Offer screen
        self.offer_screen = OfferScreen()
        screen = Screen(name='offer')
        screen.add_widget(self.offer_screen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == '__main__':
    trade_app = kandam()
    trade_app.run()
'''
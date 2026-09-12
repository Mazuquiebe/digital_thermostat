from machine import Pin, ADC
from display import Display


class Menu:
    def __init__(self, 
                 clk_pin: int = 0, 
                 dio_pin: int = 1):
        
        self.display = Display(clk_pin=clk_pin, dio_pin=dio_pin)
        self.menu_options = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10" ]
        self.current_option_index = 0
        self.current_option = self.menu_options[self.current_option_index]
        self.show_menu = False
        
        self.plus_button  = Pin(6, Pin.IN, Pin.PULL_DOWN)  
        self.minus_button = Pin(7, Pin.IN, Pin.PULL_DOWN)  
        self.mode_button  = Pin(8, Pin.IN, Pin.PULL_DOWN)  
        self.set_button   = Pin(9, Pin.IN, Pin.PULL_DOWN) 



    def display_menu(self):
        if self.show_menu:
            self.display.show(self.menu_options[self.current_option_index])
            
            for i, option in enumerate(self.menu_options):
                if i == self.current_option_index:
                    self.display.show(option)
                else:
                    self.display.show(option)


    def next_option(self):
        if self.current_option_index == len(self.menu_options) - 1:
            
            self.current_option_index = self.current_option_index
        else:
            self.current_option_index = self.current_option_index + 1
        self.display_menu()


    def previous_option(self):
        if self.current_option_index == 0:
            self.current_option_index = 0
        else:
            self.current_option_index = self.current_option_index - 1
        self.display_menu()


    def select_option(self):
        selected_option = self.menu_options[self.current_option_index]
        self.display.show(selected_option)

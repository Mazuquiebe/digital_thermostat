from asyncio import sleep

from tm1637 import TM1637
from machine import Pin, ADC
from utime import sleep


class Display(TM1637):
    def __init__(self, clk_pin: int = 0, dio_pin: int = 1):
        super().__init__(clk=Pin(clk_pin, Pin.OUT), dio=Pin(dio_pin, Pin.OUT))
        
    def scroll_message(self, message: str, delay: float = 0.5):
        for m in (message):
                msg_length = len(message)
                m_index = message.index(m)
                
                if message.index(m) >= msg_length-1:
                    self.show(f"{m}")
                    sleep(0.5)  
                else:
                    self.show(message[m_index:msg_length])
                    sleep(0.5)  
                    self.show("    ")
        
        self.show("    ")
    
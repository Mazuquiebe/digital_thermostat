from tm1637 import TM1637
from machine import Pin, ADC


class Display(TM1637):
    def __init__(self, clk_pin: int = 0, dio_pin: int = 1):
        super().__init__(clk=Pin(clk_pin, Pin.OUT), dio=Pin(dio_pin, Pin.OUT))

import json
from machine import Pin, ADC
from utime import ticks_ms,ticks_diff, sleep   
import thermistor
from tm1637 import TM1637

from settings import Settings
from compressor import Compressor
from display import Display
from menu import Menu


class TemperatureController:
    def __init__(self,
             #pins for the peripherals
             display_clk_pin:int, 
             display_dio_pin:int,
             temp_sensor_pin:int,
             defrost_sensor_pin:int,
             compressor_pin:int, 
                              
             #parameters for the temperature controller
             password: int = 123, 
             target_temperature: int = 2, 
             maximum_permitted_temperature: int = 4,
             minimum_permitted_temperature: int = -4, 
             hysteresis: int = 2, defrost_interval: int = 17000,
             defrost_duration: int = 1800):
        
        
        self.parameters = Settings(password, 
                                   target_temperature, 
                                   maximum_permitted_temperature,
                                   minimum_permitted_temperature, 
                                   hysteresis,
                                   defrost_duration).parameters
        
        
        self.display = Display(clk_pin=display_clk_pin, 
                               dio_pin=display_dio_pin)
        
        self.temp_sensor = ADC(Pin(temp_sensor_pin))
        self.defrost_sensor = ADC(Pin(defrost_sensor_pin))
        
        self.compressor = Compressor(compressor_pin)
        self.menu = Menu(settings=self.parameters, 
                         clk_pin=display_clk_pin, 
                         dio_pin=display_dio_pin)
            
        
    def calculate_temperature_in_celsius(self, adc_value: int):
        Vout = (3.3 / 65535) * adc_value
        TempC = thermistor.thermistorTemp(Vout)
        return TempC
    
    
    def check_temperature(self,):
        adc_value = self.temp_sensor.read_u16()
        return self.calculate_temperature_in_celsius(adc_value)


    def check_defrost_sensor(self):
        adc_value = self.defrost_sensor.read_u16()
        return self.calculate_temperature_in_celsius(adc_value)
    
    
    def display_temperature(self, temperature: float):
        msg = f"{int(temperature)}*C"
        self.display.show(msg)
        
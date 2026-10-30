from machine import Pin, ADC
from utime import ticks_ms,ticks_diff, sleep   
import thermistor
from settings import Settings
from compressor import Compressor
from display import Display
from menu import Menu


class TemperatureController:
    def __init__(self,
                 #paratmeters for the controller settings
                 parameters: Settings,
                 menu: Menu,
                 display: Display,
                 compressor: Compressor,
                 #pins for the peripherals
                 temp_sensor_pin:int,
                 defrost_sensor_pin:int,
                 ):
        
        self.parameters = parameters
        self.display = display
        self.compressor = compressor
        self.menu = menu
        
        self.temp_sensor = ADC(Pin(temp_sensor_pin))
        self.defrost_sensor = ADC(Pin(defrost_sensor_pin))
        
        
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
        
        
    def animated_message(self, msg: str):
        for m in msg:
            msg_length = len(msg)
            m_index = msg.index(m)
            
            if msg.index(m) >= msg_length-1:
                self.display.show(f"{m}")
                sleep(0.5)  
            else:
                self.display.show(msg[m_index:msg_length])
                sleep(0.5)  
                self.display.show("    ")
      
        self.display.show("    ")
  
import json
from machine import Pin, ADC

from tm1637 import TM1637


class Compressor:
    def __init__(self, pin: int):
        self.pin = Pin(pin, Pin.OUT)
        self.is_on = False
        self.time_running = 0

    def turn_on(self):
        self.is_on = True
        self.pin.value(1)
        print("Compressor turned ON.")

    def turn_off(self):
        self.is_on = False
        self.pin.value(0)  
        print("Compressor turned OFF.")
        
        
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
        
        self.display = TM1637(clk=Pin(display_clk_pin, Pin.OUT), 
                              dio=Pin(display_dio_pin, Pin.OUT))
        
        self.temp_sensor = ADC(Pin(temp_sensor_pin))
        self.defrost_sensor = ADC(Pin(defrost_sensor_pin))
        
        self.compressor = Compressor(compressor_pin)
        
        self.password = password
        self.target_temperature = target_temperature
        self.maximum_permitted_temperature = maximum_permitted_temperature
        self.minimum_permitted_temperature = minimum_permitted_temperature
        self.hysteresis = hysteresis
        self.defrost_interval = defrost_interval
        self.defrost_duration = defrost_duration
        self.settings = {
            "password": self.password,
            "target_temperature": self.target_temperature,
            "maximum_permitted_temperature": self.maximum_permitted_temperature,
            "minimum_permitted_temperature": self.minimum_permitted_temperature,
            "hysteresis": self.hysteresis,
            "defrost_interval": self.defrost_interval,
            "defrost_duration": self.defrost_duration,
        }
        self.save_settings()  # Save settings to file
        self.load_settings()
        

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                loaded_settings = json.load(f)
                self.settings.update(loaded_settings)
        except FileNotFoundError:
            self.save_settings()  # Save default settings if file doesn't exist
        except json.JSONDecodeError:
            print("Error decoding settings.json. Using default settings.")
            self.save_settings()  # Save default settings if JSON is invalid


    def save_settings(self):
        with open("settings.json", "w") as f:
            json.dump(self.settings, f)


    def set_target_temperature(self, temp: int):
        self.settings["target_temperature"] = temp
        self.save_settings()


    def set_hysteresis(self, hyst: int):
        self.settings["hysteresis"] = hyst
        self.save_settings()

        
    def update_setting(self, key: str, value):
        if key in self.settings:
            self.settings[key] = value
            self.save_settings()
        else:
            raise KeyError(f"Setting '{key}' does not exist.")

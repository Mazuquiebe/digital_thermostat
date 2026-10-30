from machine import Pin
import json


class Settings:
        
    def __init__(self, password: int = 123, 
                 target_temperature: int = 2, 
                 maximum_permitted_temperature: int = 4,
                 minimum_permitted_temperature: int = -4, 
                 hysteresis: int = 2, 
                 defrost_interval: int = 17000,
                 defrost_duration: int = 1800):
       
        self.parameters = self.load_settings()
        if self.parameters is None:
            self.parameters = {
                "password": password,
                "target_temperature": target_temperature,
                "maximum_permitted_temperature": maximum_permitted_temperature,
                "minimum_permitted_temperature": minimum_permitted_temperature,
                "hysteresis": hysteresis,
                "defrost_interval": defrost_interval,
                "defrost_duration": defrost_duration,
            }
        self.save_settings(self.parameters)
            
            
    
    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                loaded_settings = json.load(f)
                return loaded_settings
        except FileNotFoundError:
            raise FileNotFoundError("Settings file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding settings.json. Using default settings.")


    def save_settings(self, parameters: dict):
        with open("settings.json", "w") as f:
            json.dump(self.parameters, f)
        return self.parameters

          
    def update_setting(self, key: str, value):
        if self.parameters is not None and key in self.parameters:
            self.parameters[key] = value
            self.save_settings(self.parameters)
        else:
            raise KeyError(f"Setting '{key}' does not exist.")
 
     
                 
     
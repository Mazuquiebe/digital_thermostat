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
            
        self.parameters = {
            "password": password,
            "target_temperature": target_temperature,
            "maximum_permitted_temperature": maximum_permitted_temperature,
            "minimum_permitted_temperature": minimum_permitted_temperature,
            "hysteresis": hysteresis,
            "defrost_interval": defrost_interval,
            "defrost_duration": defrost_duration,
        }
        self.save_settings()
            
            
    
    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                loaded_settings = json.load(f)
                self.parameters.update(loaded_settings)
        except FileNotFoundError:
            self.save_settings()  # Save default settings if file doesn't exist
        except json.JSONDecodeError:
            print("Error decoding settings.json. Using default settings.")
            self.save_settings()  # Save default settings if JSON is invalid


    def save_settings(self):
        with open("settings.json", "w") as f:
            json.dump(self.parameters, f)
        return self.parameters


    def set_target_temperature(self, temp: int):
        self.parameters["target_temperature"] = temp
        self.save_settings()

    def set_hysteresis(self, hyst: int):
        
        self.parameters["hysteresis"] = hyst
        self.save_settings()
        
            
    def update_setting(self, key: str, value):
            
        if key in self.parameters:
            self.parameters[key] = value
            self.save_settings()
        else:
            raise KeyError(f"Setting '{key}' does not exist.")
 
     
                 
     
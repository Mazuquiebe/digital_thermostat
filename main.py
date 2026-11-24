from time import sleep

from compressor import Compressor
import json

from display import Display
from settings import Settings
from temperatureController import TemperatureController
from menu import Menu


display = Display(clk_pin=0, dio_pin=1)
settings = Settings()
compressor = Compressor(2)
menu = Menu(settings=settings.parameters, display=display)

controller = TemperatureController(
    menu=menu,
    parameters=settings,
    temp_sensor_pin=26,
    defrost_sensor_pin=27,
    compressor=compressor,
    display=display
)


# def load_settings():
    
#     with open("settings.json", "r") as f:
#         loaded_settings = json.load(f)
#         print("Loaded settings:", loaded_settings)
#         return loaded_settings

# load_settings()
controller.compressor.is_on        
while True: 
    
    temperature = controller.check_temperature()

    msg = f"{int(temperature)}*Celcius"

    # controller.display.show("1234")
    if(controller.compressor.is_on and temperature > controller.parameters["max_temp"]) or (controller.compressor.is_on and temperature < controller.parameters["min_temp"]):
        controller.compressor.turn_off()
    elif controller.compressor.is_off and temperature < controller.parameters["target_temp"]:
        controller.compressor.turn_on()
        
    display.scroll(msg)
    
print("Finished.")

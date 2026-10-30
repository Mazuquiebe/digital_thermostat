from compressor import Compressor
from display import Display
from settings import Settings
from temperatureController import TemperatureController
from menu import Menu

from utime import sleep


display = Display(clk_pin=0, dio_pin=1)
settings = Settings()
compressor = Compressor(2)  #the compressor output is connected to GPIO pin 2
menu = Menu(settings=settings.parameters, display=display)

controller = TemperatureController(
    menu=menu,
    parameters=settings,
    temp_sensor_pin=26,
    defrost_sensor_pin=27,
    compressor=compressor,
    display=display
)

while True: 
    
    temperature = controller.check_temperature()
    controller.display_temperature(temperature)

    msg = f"{int(temperature)}*Celcius"
    sleep(5)

    controller.display.scroll_message(msg)
    
print("Finished.")

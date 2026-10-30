from compressor import Compressor
from display import Display
from settings import Settings
from tm1637 import TM1637
from machine import Pin, ADC

from utime import sleep
import thermistor
from temperatureController import TemperatureController
from menu import Menu


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

# display = controller.display
# tempSensor = controller.temp_sensor
# defrostSensor = controller.defrost_sensor

# compressorOut = Pin(2, Pin.OUT)  #the compressor output is connected to GPIO pin 2
# heaterOut = Pin(3, Pin.OUT)  #the heater output is connected to GPIO pin 3

# plusButton = Pin(6, Pin.IN, Pin.PULL_DOWN)  #the plus button is connected to GPIO pin 6
# minusButton = Pin(7, Pin.IN, Pin.PULL_DOWN)  #the minus button is connected to GPIO pin 7
# modeButton = Pin(8, Pin.IN, Pin.PULL_DOWN)  #the mode button is connected to GPIO pin 8
# setButton = Pin(9, Pin.IN, Pin.PULL_DOWN)  #the set button is connected to GPIO pin 9

    
while True: 
    
    temperature = controller.check_temperature()
    controller.display_temperature(temperature)

    msg = f"{int(temperature)}*Celcius"
    sleep(5)

    controller.animated_message(msg)
    
print("Finished.")

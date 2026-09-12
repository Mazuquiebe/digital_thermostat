from tm1637 import TM1637
from machine import Pin, ADC

from utime import sleep
import thermistor
from temperatureController import TemperatureController

controller = TemperatureController(
    display_clk_pin=0,
    display_dio_pin=1,
    temp_sensor_pin=26,
    defrost_sensor_pin=27,
    compressor_pin=2
)

display = controller.display
tempSensor = controller.temp_sensor
defrostSensor = controller.defrost_sensor

compressorOut = Pin(2, Pin.OUT)  #the compressor output is connected to GPIO pin 2
heaterOut = Pin(3, Pin.OUT)  #the heater output is connected to GPIO pin 3

plusButton = Pin(6, Pin.IN, Pin.PULL_DOWN)  #the plus button is connected to GPIO pin 6
minusButton = Pin(7, Pin.IN, Pin.PULL_DOWN)  #the minus button is connected to GPIO pin 7
modeButton = Pin(8, Pin.IN, Pin.PULL_DOWN)  #the mode button is connected to GPIO pin 8
setButton = Pin(9, Pin.IN, Pin.PULL_DOWN)  #the set button is connected to GPIO pin 9






def calculate_temperature_in_celsius():
    adc = tempSensor.read_u16()
    Vout = (3.3 / 65535) * adc
    TempC = thermistor.thermistorTemp(Vout)
    return TempC 
   
     
while True: 
    TempC = calculate_temperature_in_celsius()

    msg = f"{int(TempC)}*Celcius"
    display.show(msg)
    sleep(5)
    
    for m in msg:
        msg_length = len(msg)
        m_index = msg.index(m)
        
        if msg.index(m) >= msg_length-1:
            display.show(f"{m}")
            sleep(0.5)  
        else:
            display.show(msg[m_index:msg_length])
            sleep(0.5)  
            display.show("    ")
  
    display.show("    ")
    
print("Finished.")

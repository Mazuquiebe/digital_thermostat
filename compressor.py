from machine import Pin

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
        
   
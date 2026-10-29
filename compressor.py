from machine import Pin

class Compressor:
    def __init__(self, pin: int):
        self.pin = Pin(pin, Pin.OUT)
        self.is_on = False
        self.time_running = 0

    def turn_on(self):
        self.pin.value(1)
        self.is_on = self.pin.value
        print("Compressor turned ON.")

    def turn_off(self):
        self.pin.value(0)  
        self.is_on = self.pin.value
        print("Compressor turned OFF.")
        
   
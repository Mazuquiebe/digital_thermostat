# Digital Thermostat — Work in Progress

Experimental MicroPython firmware for a temperature controller based on the Raspberry Pi Pico. The project reads a thermistor, displays the reading on a four-digit TM1637 display, and controls an output for a compressor.

## Hardware

| Component | GPIO |
| --- | ---: |
| TM1637 display - CLK | 0 |
| TM1637 display - DIO | 1 |
| Compressor control output | 2 |
| Main thermistor (ADC) | 26 |
| Defrost sensor (ADC) | 27 |
| +, -, mode, and set buttons | 6, 7, 8, and 9 |

The thermistor should be connected in a voltage divider compatible with the Pico's ADC inputs. The conversion in [thermistor.py](./thermistor.py) uses a 3.3 V supply, a 10 kΩ reference resistor, and specific Steinhart–Hart constants; adjust these constants if you use a different sensor.

**Safety:** Never connect a compressor directly to a Pico GPIO pin. Use a properly rated, isolated driver, and take appropriate precautions when working with mains voltage.

## Setup

1. Install the appropriate MicroPython firmware on the Raspberry Pi Pico.
2. Copy the project's `.py` files to the device, keeping them in the same folder. `tm1637.py` is included.
3. Run `main.py` on the device. If it is placed in the root of the Pico's filesystem, MicroPython may also run it at startup.

There are no external dependencies beyond MicroPython and the hardware modules included in its firmware (`machine` and `utime`).

## Current behavior

The main program reads the sensor connected to GPIO 26 and converts the ADC reading to Celsius. In the main loop, it turns the compressor output on when the temperature is below 0 °C; otherwise, it turns the output off, waits five seconds, and scrolls the temperature across the display.

The parameters in [settings.py](./settings.py) include a target temperature, limits, hysteresis, and defrost settings. These parameters do not currently control the main loop. The `Settings` class also writes the default values to `settings.json` when initialized. Defrost sensor reading and the menu are present in the code, but they are not yet integrated into a functional control cycle.

## Project structure

- `main.py` — initializes the components and runs the main loop.
- `temperatureController.py` — reads the sensors and converts readings to Celsius.
- `thermistor.py` — calculates temperature from the divider voltage.
- `compressor.py` — controls the compressor GPIO output.
- `display.py` and `tm1637.py` — display interface and driver.
- `menu.py` — initial implementation of the button interface.
- `settings.py` and `settings.json` — controller settings.

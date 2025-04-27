#verify ohms law with a pico

from machine import Pin
import time

# Set GPIO15 as output
led_pin = Pin(15, Pin.OUT)

try:
    while True:
        led_pin.value(1)  # Turn on LED
        time.sleep(2)
        #led_pin.value(0)  # Turn off LED
        time.sleep(2)
except:
    led_pin.value(0)
    
print("exited")
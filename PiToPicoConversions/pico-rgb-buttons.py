#pico-rgb-buttons.py
from machine import Pin
from time import sleep
import utils
rPin = Pin(16, Pin.OUT)
gPin = Pin(17, Pin.OUT)
bPin = Pin(18, Pin.OUT)

rButton = Pin(19, Pin.IN, Pin.PULL_DOWN)
gButton = Pin(20, Pin.IN, Pin.PULL_DOWN)
bButton = Pin(21, Pin.IN, Pin.PULL_DOWN)

try:
    while True:
        rPin.value(False)
        gPin.value(False)
        bPin.value(False)
        
        if rButton.value() == True:
            rPin.value(True)
            print("Red Pressed!")
        if gButton.value() == True:
            gPin.value(True)
            print("Green Pressed!")
        if bButton.value() == True:
            bPin.value(True)
            print("Blue Pressed!")
        sleep(.2)
except:
    print("interrupted pico")

utils.pin_cleanup(rPin)
utils.pin_cleanup(gPin)
utils.pin_cleanup(bPin)
from machine import Pin
from time import sleep
import utils
rPin = Pin(13, Pin.OUT)
gPin = Pin(12, Pin.OUT)
bPin = Pin(11, Pin.OUT)
    #dimmerButtonPin = Pin(17, Pin.IN, Pin.PULL_UP)



rPin.value(True)
sleep(.6)
gPin.value(True)
sleep(.6)
bPin.value(True)

sleep(.6)
utils.pin_cleanup(rPin)
utils.pin_cleanup(gPin)
utils.pin_cleanup(bPin)


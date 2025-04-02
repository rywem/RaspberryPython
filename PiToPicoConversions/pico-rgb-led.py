from machine import Pin
from time import sleep
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
rPin.value(0)
rPin.value(Pin.IN)

gPin.value(0)
gPin.value(Pin.IN)

bPin.value(0)
bPin.value(Pin.IN)


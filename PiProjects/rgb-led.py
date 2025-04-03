import RPi.GPIO as GPIO
from time import sleep
# RGB led

GPIO.setmode(GPIO.BOARD)

rPin = 37
gPin = 35
bPin = 33

GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.output(bPin, True)

sleep(1)
GPIO.cleanup()
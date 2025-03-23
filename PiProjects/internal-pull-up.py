# internal pull up
import time as sleep
import RPi.GPIO as GPIO

delay=.1
inPin=40
outPin=38
GPIO.setmode(GPIO.BOARD) #physical pin numbering system
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # add a pull up resistor inside raspberry pi

try:
    while True:
        readVal=GPIO.input(inPin)
        print(readVal)
        if readVal == 1:
            GPIO.output(outPin, 0)
        if readVal == 0:
            GPIO.output(outPin, 1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO cleaned")

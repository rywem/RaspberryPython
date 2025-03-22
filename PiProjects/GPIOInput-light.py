# read 3.3v GPIO 1 with GPIO 40


import RPi.GPIO as GPIO
from time import sleep
# use the physical numbering system on the board
# instead of BCIM system
GPIO.setmode(GPIO.BOARD)
inPin = 40
GPIO.setup(inPin, GPIO.IN)
lightPin = 38
GPIO.setup(lightPin, GPIO.OUT)
try:
    while True:        
        readVal = GPIO.input(inPin) #read the value from the 40
        if readVal == 0:
            GPIO.output(lightPin, GPIO.HIGH)
        else:
            GPIO.output(lightPin, GPIO.LOW)
        print(readVal)
        sleep(1)
except KeyboardInterrupt: 
    GPIO.cleanup()
    print("ending...")

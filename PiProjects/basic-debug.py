# read 3.3v GPIO 1 with GPIO 40


import RPi.GPIO as GPIO
from time import sleep
# use the physical numbering system on the board
# instead of BCIM system
GPIO.setmode(GPIO.BOARD)

inPin = 40
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:        
        state = GPIO.input(inPin)
        #print("Button is", "PRESSED" if state else "not pressed")
        print(state)
        sleep(1)
except KeyboardInterrupt: 
    GPIO.cleanup()
    print("Cleaning, ending...")


# read 3.3v GPIO 1 with GPIO 40


import RPi.GPIO as GPIO
from time import sleep
# use the physical numbering system on the board
# instead of BCIM system
GPIO.setmode(GPIO.BOARD)
def boolToStr(input):
    if input == True:
        return "True"
    else:
        return "False"
def readValueToString(input):
    if input == 1:
        return "1"
    else:
        return "0"

inPin = 40
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lightPin = 38
GPIO.setup(lightPin, GPIO.OUT)
light = False
buttonState = 0
buttonStateOld = 0
try:
    while True:        
        readVal = GPIO.input(inPin) #read the value from the 40
        if readVal == 0:
            light = not light
            
        if light == True:
            GPIO.output(lightPin, GPIO.HIGH)
        else:
            GPIO.output(lightPin, GPIO.LOW)
        print(readValueToString(readVal) +" "+  boolToStr(light))
        
        sleep(0.5)
except KeyboardInterrupt: 
    GPIO.cleanup()
    print("ending...")

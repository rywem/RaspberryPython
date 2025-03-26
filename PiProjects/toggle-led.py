#the solution as per the instructor

from time import sleep
import RPi.GPIO as GPIO
delay = .1
inPin = 40
outPin = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
LEDState=False
buttonState=1
buttonStateOld=1

try:
    while True:
        buttonState=GPIO.input(inPin)
        print(buttonState)
        if buttonState == 1 and buttonStateOld == 0:
            LEDState = not LEDState
            GPIO.output(outPin,LEDState)
        
        buttonStateOld=buttonState
        sleep(delay)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print("cleaning and exiting")
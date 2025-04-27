# analog-joystick.py

import RPi.GPIO as GPIO
import time
import ADC0834

GPIO.setmode(GPIO.BCM)

buttonPin = 21
ADC0834.setup()

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        analogValX = ADC0834.getResult(0)
        analogValY = ADC0834.getResult(1)        
        buttonState = GPIO.input(buttonPin)
        
        print(f"x: {analogValX}, Y: {analogValY}, Btn: {buttonState}")
        time.sleep(.1)
except KeyboardInterrupt:    
    GPIO.cleanup()
    print("GPIO cleaned, program exited")
    

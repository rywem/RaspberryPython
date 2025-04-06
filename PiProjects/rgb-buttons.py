# rgb-buttons.py
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

rPin = 37
gPin = 35
bPin = 33

rButton = 36
gButton = 38
bButton = 40

GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.output(rPin, 0)
GPIO.output(gPin, 0)
GPIO.output(bPin, 0)

GPIO.setup(rButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

rState = 0
gState = 0
bState = 0

rStateOld = 0
gStateOld = 0
bStateOld = 0

rDC = .9
gDC = .9
bDC = .9

#rPWM = GPIO.PWM(rPin,100)
#gPWM = GPIO.PWM(rPin,100)
#bPWM = GPIO.PWM(rPin,100)

GPIO.output(rPin, False)
GPIO.output(gPin, False)
GPIO.output(bPin, False)
rBP = 1
bBP = 1
gBP = 1
try:
    
    while True:
        #GPIO.output(rPin, False)
        #GPIO.output(gPin, False)
        #GPIO.output(bPin, False)
        rState = GPIO.input(rButton)
        gState = GPIO.input(gButton)
        bState = GPIO.input(bButton)        
        if rState != rStateOld:
            rState = rStateOld            
            GPIO.output(rPin, True)
            GPIO.output(gPin, False)
            GPIO.output(bPin, False)
            print("red pressed")
        if gState != gStateOld:
            gState = gStateOld
            GPIO.output(rPin, False)
            GPIO.output(gPin, True)            
            GPIO.output(bPin, False)
            print("Green pressed")
        if bState != bStateOld:
            bState = bStateOld
            GPIO.output(rPin, False)
            GPIO.output(gPin, False)
            GPIO.output(bPin, True)
            print("Blue pressed")
        
        sleep(.2)
        
except KeyboardInterrupt:
    print("cleanup complete.")
    GPIO.cleanup()
    
GPIO.cleanup()
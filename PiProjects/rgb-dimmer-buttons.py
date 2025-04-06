#rgb dimmer buttons
# rgb-buttons.py
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

rLedPin = 37
gLedPin = 35
bLedPin = 33

rButton = 36
gButton = 38
bButton = 40
modeButton = 32
GPIO.setup(rLedPin, GPIO.OUT)
GPIO.setup(gLedPin, GPIO.OUT)
GPIO.setup(bLedPin, GPIO.OUT)

#GPIO.output(rLedPin, 0)
#GPIO.output(gLedPin, 0)
#GPIO.output(bLedPin, 0)

GPIO.setup(rButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(modeButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
modeState = 1
modeStateOld = 1
rState = 0
gState = 0
bState = 0

rStateOld = 0
gStateOld = 0
bStateOld = 0

rDC = .9
gDC = .9
bDC = .9

rPWM = GPIO.PWM(rLedPin,100)
gPWM = GPIO.PWM(gLedPin,100)
bPWM = GPIO.PWM(bLedPin,100)

GPIO.output(rLedPin, False)
GPIO.output(gLedPin, False)
GPIO.output(bLedPin, False)
rBP = 1
bBP = 1
gBP = 1
rDutyCycle = 1.01
gDutyCycle = 1.01
bDutyCycle = 1.01

rDutyCycleOld = 1.01
gDutyCycleOld = 1.01
bDutyCycleOld = 1.01
rPWM.start(rDutyCycle)
gPWM.start(gDutyCycle)
bPWM.start(bDutyCycle)
stateChangeType = "Increase"
try:
    
    while True:
        rState = GPIO.input(rButton)
        gState = GPIO.input(gButton)
        bState = GPIO.input(bButton)
        modeState = GPIO.input(modeButton)
        if modeState == 1:
            modeStateOld = not modeStateOld
            if modeStateOld == 1:
                print("Mode State: Increase")
                stateChangeType = "Increase"
            else:
                print("Mode State: Decrease")
                stateChangeType = "Decrease"
        if rState == 1:
            if modeStateOld == 1:
                rBP += 1
            else:
                rBP -= 1                
            rDutyCycle = (1.5849) ** rBP
            print("Red: ", stateChangeType)
        if gState == 1:
            if modeStateOld == 1:
                gBP += 1
            else:
                gBP -= 1                            
            gDutyCycle = (1.5849) ** gBP
            print("Green: ", stateChangeType)
        if bState == 1:
            if modeStateOld == 1:
                bBP += 1
            else:
                bBP -= 1                            
            bDutyCycle = (1.5849) ** bBP
            print("Blue: ", stateChangeType)
            
        rBP = max(min(rBP, 10), 1)
        gBP = max(min(gBP, 10), 1)
        bBP = max(min(bBP, 10), 1)
        rDutyCycle = max(min(rDutyCycle, 99), 1)
        gDutyCycle = max(min(gDutyCycle, 99), 1)
        bDutyCycle = max(min(bDutyCycle, 99), 1)
        
        if rDutyCycle != rDutyCycleOld:
            rPWM.ChangeDutyCycle(rDutyCycle)
            rDutyCycleOld = rDutyCycle
            print("Red Duty Cycle:", rDutyCycle)
        if gDutyCycle != gDutyCycleOld:
            gPWM.ChangeDutyCycle(gDutyCycle)
            gDutyCycleOld = gDutyCycle
            print("Green Duty Cycle:", gDutyCycle)
        if bDutyCycle != bDutyCycleOld:
            bPWM.ChangeDutyCycle(bDutyCycle)
            bDutyCycleOld = bDutyCycle
            print("Blue Duty Cycle:", bDutyCycle)
            
        sleep(.15)
        
except KeyboardInterrupt:
    print("cleanup complete.")
    GPIO.cleanup()
    
GPIO.cleanup()

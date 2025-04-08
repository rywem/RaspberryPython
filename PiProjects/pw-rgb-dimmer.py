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
rButState = 0
gButState = 0
bButState = 0

rButStateOld = 0
gButStateOld = 0
bButStateOld = 0

rPWM = GPIO.PWM(rLedPin,100)
gPWM = GPIO.PWM(gLedPin,100)
bPWM = GPIO.PWM(bLedPin,100)

GPIO.output(rLedPin, False)
GPIO.output(gLedPin, False)
GPIO.output(bLedPin, False)
rBP = 1
bBP = 1
gBP = 1
rDutyCycle = .99
gDutyCycle = .99
bDutyCycle = .99

rPWM.start(rDutyCycle)
gPWM.start(gDutyCycle)
bPWM.start(bDutyCycle)

excepted = False
try:
    
    while True:
        rButState = GPIO.input(rButton)
        gButState = GPIO.input(gButton)
        bButState = GPIO.input(bButton)
        #print("Button State: R G B", rButState, gButState, bButState)
        if rButState == 1 and rButStateOld == 0:
            rDutyCycle = rDutyCycle * 1.58
            if rDutyCycle > 99:
                rDutyCycle = .99
            rPWM.ChangeDutyCycle(int(rDutyCycle))            
            print("Red channel registered, DC:", rDutyCycle)
        if gButState == 1 and gButStateOld == 0:
            gDutyCycle = gDutyCycle * 1.58
            if gDutyCycle > 99:
                gDutyCycle = .99
            gPWM.ChangeDutyCycle(int(gDutyCycle))            
            print("Green channel registered, DC:", gDutyCycle)
        if bButState == 1 and bButStateOld == 0:
            bDutyCycle = bDutyCycle * 1.58
            if bDutyCycle > 99:
                bDutyCycle = .99
            bPWM.ChangeDutyCycle(int(bDutyCycle))            
            print("Green channel registered, DC:", bDutyCycle)        
        rButStateOld = rButState
        gButStateOld = gButState
        bButStateOld = bButState
        sleep(.15)
        
except KeyboardInterrupt:
    print("cleanup complete.")
    GPIO.cleanup()
    excepted = True
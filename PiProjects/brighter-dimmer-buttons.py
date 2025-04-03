import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

ledPin = 36
dimmerButtonPin = 40
brightButtonPin = 38
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(dimmerButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(brightButtonPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
incrementValue = 15
dutyCycle = 1
dutyCycleOld = dutyCycle
myPWM = GPIO.PWM(ledPin, 100) #frequency
myPWM.start(dutyCycle)
BP = 10
try:
    while True:
        dimmerReadVal = GPIO.input(dimmerButtonPin)
        brightReadVal = GPIO.input(brightButtonPin)
        
        if dimmerReadVal == 1:
            BP=BP-1
            dutyCycle=(1.5849)**BP
        if brightReadVal == 1:
            BP=BP+1
            dutyCycle=(1.5849)**BP
        if dutyCycle > 99:
            dutyCycle = 99
        if dutyCycle < 1:
            dutyCycle = 1
        if dutyCycleOld != dutyCycle:                
            myPWM.ChangeDutyCycle(dutyCycle)
            dutyCycleOld = dutyCycle
        print(dutyCycle)
        #myPWM.start(10) #duty cycle in %
            
        sleep(.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("cleaned and exited")
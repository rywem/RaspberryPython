import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

ledPin = 37
dimmerButtonPin = 40
brightButtonPin = 38
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(dimmerButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(brightButtonPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
incrementValue = 15
lightValue = 50
lightValueOld = lightValue
myPWM = GPIO.PWM(ledPin, 100) #frequency
myPWM.start(lightValue)
try:
    while True:
        dimmerReadVal = GPIO.input(dimmerButtonPin)
        brightReadVal = GPIO.input(brightButtonPin)
        
        if dimmerReadVal == 1:
            lightValue = lightValue - incrementValue
        if brightReadVal == 1:
            lightValue = lightValue + incrementValue
        if lightValue > 100:
            lightValue = 99
        if lightValue < 0:
            lightValue = 1
        if lightValueOld != lightValue:                
            myPWM.start(lightValue)
            lightValueOld = lightValue
        print(lightValue)
        #myPWM.start(10) #duty cycle in %
            
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("cleaned and exited")
# analog input
# https://www.youtube.com/watch?v=_PnVt8XtFcw&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=18

# using analog to digital converter
import ADC0834
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#initialize the chip
ADC0834.setup()

ledPin = 20
GPIO.setup(ledPin, GPIO.OUT)

rPWM = GPIO.PWM(ledPin,100)
dutyCycle = 1
rPWM.start(dutyCycle)
try:
    while True:
        analogValue = ADC0834.getResult(1) #pass channel as a parameter
        if analogValue == 0:
            dutyCycle = 0
        else:
            dutyCycle = (analogValue/255) * 100
        rPWM.ChangeDutyCycle(dutyCycle)
        print(analogValue)
        sleep(.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Cleaned and exited')
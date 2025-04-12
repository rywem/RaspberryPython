# analog input
# https://www.youtube.com/watch?v=_PnVt8XtFcw&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=18

# using analog to digital converter
import ADC0834
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#initialize the chip
ADC0834.setup()

try:
    while True:
        analogValue = ADC0834.getResult(0) #pass channel as a parameter
        print(analogValue)
        sleep(.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Cleaned and exited')
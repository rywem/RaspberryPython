# simulate an analogue
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)



try:
    GPIO.output(37, True)
    sleep(.5)
    GPIO.output(37, False)
    sleep(.1)
    myPWM = GPIO.PWM(37, 100) #frequency
    myPWM.start(10) #duty cycle in %
    myPWM.ChangeDutyCycle(75)
    
    #while True:
     #   GPIO.output(37, True)
    sleep(2)
    myPWM.stop(10)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("cleanup complete")

GPIO.cleanup()

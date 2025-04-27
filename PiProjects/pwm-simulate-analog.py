# simulate an analogue
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

myPWM = GPIO.PWM(40, 100) #frequency

try:
#    GPIO.output(37, True)
 #   sleep(.5)
 #   GPIO.output(37, False)
  #  sleep(.1)
    
    myPWM.start(50) #duty cycle in %
    #myPWM.ChangeDutyCycle(10)
    #myPWM.ChangeFrequency(10)
    
    while True:
        #GPIO.output(37, True)
        sleep(5)
    myPWM.stop()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("cleanup complete")

GPIO.cleanup()

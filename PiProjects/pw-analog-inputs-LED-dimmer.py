import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# Setup variables
delayTime = .1
redPin = 16
dutyCycle = 0

# Setup board
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(redPin, GPIO.OUT)
# Setup PWM
pwm = GPIO.PWM(redPin, 1000)
pwm.start(dutyCycle)

try:
    while True:
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Board cleanup successful, ending program")
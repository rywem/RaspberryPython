import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# Setup variables
delayTime = .1
redPin = 20
dutyCycle = 0

# Setup board
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(redPin, GPIO.OUT)
# Setup PWM
pwm = GPIO.PWM(redPin, 1000)
pwm.start(dutyCycle)

'''
Calculate a slope:
(0,0) [255, 100]

m = (y2 - y1) / (x2 - x1)
m = (100 - 0) / (255 - 0)
m = 100 / 255 (slope)
(y - y1) = m(x - x1)
y = (100 / 255)*x
(x = potVal)
y = Duty Cycle
'''

try:
    while True:
        # read value from potentiometer
        potVal = ADC0834.getResult(0)
        if potVal == 0:
            dutyCycle = 0
        else:
            dutyCycle = (100/255) * potVal            
        if dutyCycle > 99:
            dutyCycle = 99        
        pwm.ChangeDutyCycle(dutyCycle)
        print(potVal, dutyCycle)
        sleep(delayTime)
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Board cleanup successful, ending program")
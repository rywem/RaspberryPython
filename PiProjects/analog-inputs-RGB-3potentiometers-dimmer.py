import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# Setup variables
delayTime = .1
redPin = 20
greenPin = 21
bluePin = 12
rDutyCycle = 0
gDutyCycle = 0
bDutyCycle = 0
# Setup board
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
# Setup rPWM
rPWM = GPIO.PWM(redPin, 1000)
rPWM.start(rDutyCycle)

gPWM = GPIO.PWM(greenPin, 1000)
gPWM.start(gDutyCycle)

bPWM = GPIO.PWM(bluePin, 1000)
bPWM.start(bDutyCycle)


'''
Calculate a slope:
(0,0) [255, 100]

m = (y2 - y1) / (x2 - x1)
m = (100 - 0) / (255 - 0)
m = 100 / 255 (slope)
(y - y1) = m(x - x1)
y = (100 / 255)*x
(x = rPotVal)
y = Duty Cycle
'''

try:
    while True:

        # read value from potentiometer
        rPotVal = ADC0834.getResult(0)
        gPotVal = ADC0834.getResult(1)
        bPotVal = ADC0834.getResult(2)
        if rPotVal == 0:
            rDutyCycle = 0
        else:
            rDutyCycle = (100/255) * rPotVal            
        if rDutyCycle > 99:
            rDutyCycle = 99        
        rPWM.ChangeDutyCycle(rDutyCycle)
        if gPotVal == 0:
            gDutyCycle = 0
        else:
            gDutyCycle = (100/255) * gPotVal
        if gDutyCycle > 99:
            gDutyCycle = 99        
        gPWM.ChangeDutyCycle(gDutyCycle)
        
        if bPotVal == 0:
            bDutyCycle = 0
        else:
            bDutyCycle = (100/255) * bPotVal
        if bDutyCycle > 99:
            bDutyCycle = 99
        bPWM.ChangeDutyCycle(bDutyCycle)
        
        print(f"Red PotVal: {rPotVal}, rDC:{rDutyCycle}")
        print(f"Green PotVal: {gPotVal}, gDC:{gDutyCycle}")
        print(f"Blue PotVal: {bPotVal}, bDC:{bDutyCycle}")
        sleep(delayTime)
        
except KeyboardInterrupt:
    rPWM.stop()
    GPIO.cleanup()
    print("Board cleanup successful, ending program")
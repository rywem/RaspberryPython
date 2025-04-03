# rgb-buttons.py
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

rPin = 37
gPin = 35
bPin = 33

rButton = 36
gButton = 38
bButton = 40

GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.output(rPin, 0)
GPIO.output(gPin, 0)
GPIO.output(bPin, 0)

GPIO.setup(rButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bButton, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)


try:
    
    while True:
        GPIO.output(rPin, False)
        GPIO.output(gPin, False)
        GPIO.output(bPin, False)
        if GPIO.input(rButton) == GPIO.HIGH:
            GPIO.output(rPin, True)
            print("red pressed")
        if GPIO.input(gButton) == GPIO.HIGH:
            GPIO.output(gPin, True)
            print("Green pressed")
        if GPIO.input(bButton) == GPIO.HIGH:
            GPIO.output(bPin, True)
            print("Blue pressed")
        
        sleep(.2)
        
except KeyboardInterrupt:
    print("interrupted")
    GPIO.cleanup()
    
GPIO.cleanup()
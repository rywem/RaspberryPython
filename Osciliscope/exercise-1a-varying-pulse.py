#exercise-1a-varying-pulse.py

import RPi.GPIO as GPIO
import time

pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 10000)
pwm.start(0)

try:
    while True:
        for dc in [10, 30, 50, 70, 90]:
            print(f"Changing to {dc}% duty cycle")
            pwm.ChangeDutyCycle(dc)
            time.sleep(2)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

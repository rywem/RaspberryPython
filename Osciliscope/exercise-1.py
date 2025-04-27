#exercise 1

import RPi.GPIO as GPIO
import time

pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(2, 1000)  # 1kHz
pwm.start(50)  # 50% duty cycle

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

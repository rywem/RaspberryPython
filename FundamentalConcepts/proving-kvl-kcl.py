# exercise-3-signal-bounce.py


import RPi.GPIO as GPIO
import time

# === Button pin setup ===
BUTTON_PIN = 1  # We'll use GPIO 20 for the button

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.OUT)

print("Ready to detect button presses...")

try:
    GPIO.output(BUTTON_PIN, GPIO.HIGH)
    while True:
        print("sleeping....")
        time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()

print("program ended")
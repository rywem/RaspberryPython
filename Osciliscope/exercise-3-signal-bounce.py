# exercise-3-signal-bounce.py


import RPi.GPIO as GPIO
import time

# === Button pin setup ===
BUTTON_PIN = 21  # We'll use GPIO 20 for the button

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Ready to detect button presses...")

try:
    while True:
        # Read button state
        button_state = GPIO.input(BUTTON_PIN)
        
        if button_state == GPIO.LOW:
            print("Button pressed!")
            time.sleep(0.1)  # Simple debounce delay
except KeyboardInterrupt:
    GPIO.cleanup()

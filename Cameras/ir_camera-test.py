import RPi.GPIO as GPIO
import time

IR_LED_PIN = 17  # Check your camera's documentation if it has this feature

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_LED_PIN, GPIO.OUT)

print("Turning on IR LEDs...")
GPIO.output(IR_LED_PIN, GPIO.HIGH)
time.sleep(30)  # Leave it on for 30 seconds to test
GPIO.output(IR_LED_PIN, GPIO.LOW)
GPIO.cleanup()

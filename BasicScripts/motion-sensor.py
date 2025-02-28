import RPi.GPIO as GPIO
import time

import RPi.GPIO as GPIO
import time

# Power: Connect Red wire to 3.3v pin
# GRND: Connect white wire to breadboard grnd and then breadboard to GRD pin
# Sensor: Black wire to breadboard, to 10k ohm resistor, jump to ground

SENSOR_PIN = 17  # The GPIO pin connected to the black wire

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set the pin as an input

try:
    while True:
        if GPIO.input(SENSOR_PIN):  # If the sensor detects motion
            print("Motion detected!")
        else:
            print("No motion")
        time.sleep(1)  # Wait 1 second before checking again

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Reset GPIO on exit
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
import time


SENSOR_PIN = 17  # The GPIO pin connected to the black wire
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set the pin as an input
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        if GPIO.input(SENSOR_PIN):  # If the sensor detects motion
            GPIO.output(LED_PIN, True)
            print("Motion detected!")
        else:
            GPIO.output(LED_PIN, False)
            print("No motion, no LED")        
        time.sleep(1)  # Wait 1 second before checking again
        
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Reset GPIO on exit
except:
    GPIO.cleanup()  # Reset GPIO on exit

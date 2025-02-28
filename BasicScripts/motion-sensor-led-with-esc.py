import RPi.GPIO as GPIO
import time
import sys
import select

def is_esc_pressed():
    """Check if ESC is pressed without blocking."""
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    return sys.stdin.read(1) if dr else None

def main():
    SENSOR_PIN = 17  # The GPIO pin connected to the black wire
    LED_PIN = 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    GPIO.setup(LED_PIN, GPIO.OUT)

    try:
        while True:
            if GPIO.input(SENSOR_PIN):  # If the sensor detects motion
                GPIO.output(LED_PIN, True)
                print("Motion detected!")
            else:
                GPIO.output(LED_PIN, False)
                print("No motion, no LED")

            time.sleep(0.7)  # Wait before checking again

            # Check for ESC key press
            if is_esc_pressed() == "\x1b":  # ESC key
                print("ESC pressed, exiting...")
                GPIO.cleanup()
                break

    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
    except:
        GPIO.cleanup()

main()

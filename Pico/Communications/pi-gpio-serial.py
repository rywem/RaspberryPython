import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# === Pin assignments ===
outPiFToPico = 37     # GPIO 26 (output TO Pico)
inPiFromPico = 33     # GPIO 13 (input FROM Pico)
button1 = 40          # GPIO 21
button2 = 38          # GPIO 20

# === Setup pins ===
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(outPiFToPico, GPIO.OUT)
GPIO.setup(inPiFromPico, GPIO.IN)

GPIO.output(outPiFToPico, GPIO.LOW)  # Ensure output is LOW to start

print("Pi is running. Press buttons to send signals to Pico.")
print("Listening for signals from Pico...")

try:
    while True:
        # Check Pi buttons and send signal to Pico
        if GPIO.input(button1) == GPIO.LOW:
            print("Pi: Button 1 pressed! Sending signal to Pico.")
            GPIO.output(outPiFToPico, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(outPiFToPico, GPIO.LOW)

        if GPIO.input(button2) == GPIO.LOW:
            print("Pi: Button 2 pressed! Sending signal to Pico.")
            GPIO.output(outPiFToPico, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(outPiFToPico, GPIO.LOW)

        # Check for incoming signal from Pico
        if GPIO.input(inPiFromPico) == GPIO.HIGH:
            print("Pi: Received signal from Pico!")

        sleep(0.1)  # Small delay to avoid spamming the CPU
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO cleaned up. Exiting.")

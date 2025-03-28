import RPi.GPIO as GPIO
from time import sleep

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# === Pin assignments (based on your setup) ===
outPiFToPico = 37     # GPIO 26 (output TO Pico)
inPiFromPico = 33     # GPIO 13 (input FROM Pico)
button1 = 40          # GPIO 21
button2 = 38          # GPIO 20

# === Setup GPIO pins ===
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# === Main loop ===
print("Watching buttons. Press Ctrl+C to exit.")

try:
    while True:
        if GPIO.input(button1) == GPIO.LOW:
            print("Button 1 pressed!")
        if GPIO.input(button2) == GPIO.LOW:
            print("Button 2 pressed!")
        sleep(0.1)  # debounce time
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleaned up GPIO and exited.")

from machine import Pin
import utime

# === Pin assignments ===
inPicoFromPi = Pin(15, Pin.IN)        # From Pi (pin 20)
outPicoFromPi = Pin(14, Pin.OUT)      # To Pi (pin 19)
button1 = Pin(17, Pin.IN, Pin.PULL_UP)  # Button 1 (pin 22)
button2 = Pin(16, Pin.IN, Pin.PULL_UP)  # Button 2 (pin 21)
ledFromPi = Pin(13, Pin.OUT)          # LED when Pi sends signal (pin 17)

# Ensure initial states
outPicoFromPi.value(0)
ledFromPi.value(0)

print("Pico is running. Waiting for buttons and signals...")

while True:
    # === Check Pico buttons and send signal to Pi ===
    if not button1.value():
        print("Pico: Button 1 pressed! Sending signal to Pi.")
        outPicoFromPi.value(1)
        utime.sleep(0.1)
        outPicoFromPi.value(0)

    if not button2.value():
        print("Pico: Button 2 pressed! Sending signal to Pi.")
        outPicoFromPi.value(1)
        utime.sleep(0.1)
        outPicoFromPi.value(0)

    # === Check for signal from Pi and light LED ===
    if inPicoFromPi.value() == 1:
        print("Pico: Received signal from Pi! Lighting LED.")
        ledFromPi.value(1)
    else:
        ledFromPi.value(0)

    utime.sleep(0.1)

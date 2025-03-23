import machine
import utime

# Use internal pull-up on input pin
pinIn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# Set output pin (no pull-up needed for output)
pinLight = machine.Pin(14, machine.Pin.OUT)

try:
    while True:
        readVal = pinIn.value()  # Will be 1 when NOT pressed (pulled up), 0 when pressed (grounded)
        print(readVal)

        if readVal == 0:
            pinLight.value(1)  # Turn on light
        else:
            pinLight.value(0)  # Turn off light

        utime.sleep(0.3)

except KeyboardInterrupt:
    # Not strictly needed on Pico, but you can reset output pin as input if you want to 'clean up'
    pinIn = machine.Pin(15, machine.Pin.IN)
    pinLight = machine.Pin(14, machine.Pin.IN)
    print("Pins reset")

from machine import Pin, PWM
from time import sleep

# Pin definitions (use GP pin numbers)
ledPin = PWM(Pin(28))  # GP28 corresponds to physical pin 34
dimmerButtonPin = Pin(26, Pin.IN, Pin.PULL_UP)  # GP26 = pin 31
brightButtonPin = Pin(27, Pin.IN, Pin.PULL_UP)  # GP27 = pin 32

# Set PWM frequency
ledPin.freq(200)

# Initial duty cycle value
incrementValue = 15
lightValue = 50  # in percentage
lightValueOld = lightValue

# Helper function to set duty cycle (MicroPython uses 16-bit range)
def set_duty_cycle(pwm, percent):
    # Clamp the value between 0 and 100
    percent = max(1, min(99, percent))
    duty = int((percent / 100) * 65535)
    pwm.duty_u16(duty)

# Initialize with initial brightness
set_duty_cycle(ledPin, lightValue)

try:
    while True:
        if not dimmerButtonPin.value():  # active LOW
            lightValue -= incrementValue
        if not brightButtonPin.value():  # active LOW
            lightValue += incrementValue

        lightValue = max(1, min(99, lightValue))  # clamp between 1 and 99

        if lightValue != lightValueOld:
            set_duty_cycle(ledPin, lightValue)
            lightValueOld = lightValue
            print("Light value:", lightValue)

        sleep(0.1)

except KeyboardInterrupt:
    ledPin.duty_u16(0)
    print("Exiting cleanly.")

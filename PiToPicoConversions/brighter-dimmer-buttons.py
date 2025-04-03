from machine import Pin, PWM
from time import sleep

# Pin definitions (use GP pin numbers)
ledPin = PWM(Pin(13))  

dimmerButtonPin = Pin(17, Pin.IN, Pin.PULL_UP) 
brightButtonPin = Pin(16, Pin.IN, Pin.PULL_UP) 

# Set PWM frequency
ledPin.freq(200)

# Initial duty cycle value
incrementValue = 15
dutyCycle = 50  # in percentage
dutyCycleOld = dutyCycle
BP = 10
# Helper function to set duty cycle (MicroPython uses 16-bit range)
def set_duty_cycle(pwm, percent):
    # Clamp the value between 0 and 100
    percent = max(1, min(99, percent))
    '''
    MicroPython's PWM duty cycle uses a 16-bit range from 0-65535
    instead of 0-100%. So we convert the % to the equivalent value
    50% => (50/100)*65535 = 32767.5 => 32767
    25% => 16383, 75% => 491511 etc
    '''
    duty = int((percent / 100) * 65535)
    # Sets the PWM duty cycle to the calculated value
    pwm.duty_u16(duty)

# Initialize with initial brightness
set_duty_cycle(ledPin, dutyCycle)

try:
    while True:
        if not dimmerButtonPin.value():  # active LOW
            BP = BP - 1                    
        if not brightButtonPin.value():  # active LOW
            BP = BP+1
        print(BP)
        BP = max(1, min(BP, 10))
        dutyCycle = (1.5849)**BP            
        dutyCycle = max(1, min(99, dutyCycle))  # clamp between 1 and 99

        if dutyCycle != dutyCycleOld:
            set_duty_cycle(ledPin, dutyCycle)
            dutyCycleOld = dutyCycle
            print("Light value:", dutyCycle)

        sleep(0.2)

except KeyboardInterrupt:
    ledPin.duty_u16(0)
    print("Exiting cleanly.")

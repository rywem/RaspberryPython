import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pwmPin = 4 #bcm

# period needs one cycle = 20ms (.02 seconds)
frequency = 50 # hz = 1 / PERIOD in seconds = 1 / .02

# Duty Cycle approx = 1%-2% => 0 angle
# Duty Cycle aprox = 10%-15% => 180 angle

GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)

pwm.start(0)

try:
    while True:
        pwmPercent = float(input('PWM %: '))
        print(pwmPercent)
        pwm.ChangeDutyCycle(pwmPercent)
        
        time.sleep(.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program ended. Cleanup completed.")
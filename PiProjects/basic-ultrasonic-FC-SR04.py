#echo location / sonar

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


triggerPin = 23
echoPin = 24

GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(triggerPin, GPIO.OUT)

try:
    while True:
        print("triggering pin")
        GPIO.output(triggerPin,0)
        time.sleep(2E-6)
        GPIO.output(triggerPin, 1)
        time.sleep(10E-6)
        GPIO.output(triggerPin, 0)        
        while GPIO.input(echoPin) == 0:
            pass
        echoStartTime = time.time()
        while GPIO.input(echoPin) == 1:            
            pass
        echoStopTime = time.time()
        pingTravelTime = echoStopTime - echoStartTime
        print(int(pingTravelTime * 1E6) )
        distanceFt = 0
        if pingTravelTime != 0:            
            distanceCm = (pingTravelTime * 34300) / 2
            distanceFt = (distanceCm / 2.54 / 12)
        print(f"Distance (Ft): {distanceFt:.2f}")
        time.sleep(.2)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleanup complete, exiting program...")



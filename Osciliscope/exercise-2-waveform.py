import RPi.GPIO as GPIO
import time

# === PWM output pin ===
PWM_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start at 1kHz, 50% duty cycle
pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(50)

# Frequencies to try 
frequencies = [100, 500, 1000, 5000, 10000]

try:
    for freq in frequencies:
        try:
            print(f"\nChanging frequency to {freq} Hz")
            pwm.ChangeFrequency(freq)
            # Watch how the wave compresses on the oscilloscope
            time.sleep(3)
        except Exception as e:
            print(f"⚠️ Skipped {freq} Hz due to error: {e}")

except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    pwm.stop()
    GPIO.cleanup()

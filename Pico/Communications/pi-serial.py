# PI simple script to communicate between a pico and a pi

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

ser.flush()

def send_message(message):
    ser.write((message + "\n").encode('utf-8'))
    
def receive_message():
    if ser.in_waiting > 0:
        return ser.readline().decode('utf-8').strip()
    return None

counter = 0
while counter < 100:
    send_message("ping")
    start_time = time.time()
    print(time.time() - start_time)
    while time.time() - start_time < 5: #wait 5 seconds for a reply
        response = receive_message()
        if response:
            print(f"Received from PICO: {response}")
            break
        time.sleep(0.1)
    counter = counter + 1
    time.sleep(0.5)
    
ser.close()

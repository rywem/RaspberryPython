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
    response = receive_message()
    if response:
        print(f"Received from PICO: {response}")
        #break
    time.sleep(0.1)
    counter = counter + 1
    time.sleep(0.5)
    
ser.close()

'''


import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def send_message(message):
    ser.write((message + "\n").encode('utf-8'))

def receive_message():
    if ser.in_waiting > 0:
        return ser.readline().decode('utf-8').strip()
    return None

counter = 0

# Send an initial message
send_message("Hello Pico from Pi")

while counter < 1000:
    response = receive_message()
    if response:
        print(f"Received from Pico: {response}")
    time.sleep(0.1)
    counter += 1

ser.close()

def send_message(message):
    uart.write(message + "\n")

def receive_message():
    if uart.any():
        message = uart.read().decode('utf-8').strip()
        return message
    return None
counter = 0
while True:
    send_message(f"Hello from Pico, count: {counter}")
    counter = counter + 1
    utime.sleep(0.3)
    
    '''

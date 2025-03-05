import machine
import utime

# Simple script to communicate between a pi and a pico
# PICO Script
# open a direct connection over USB
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

def send_message(message):
    uart.write(message + "\n")

def receive_message():
    if uart.any():
        message = uart.read().decode('utf-8').strip()
        return message
    return None

while True:
    message = receive_message()
    if message:
        print(f"Received: {message}")
        if message == "ping":
            send_message("pong")
        else:
            send_message(f"Echo: {message}")
    utime.sleep(0.1)
        

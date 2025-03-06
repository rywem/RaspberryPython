import utime
import sys
import select
import machine

button = machine.Pin(14, machine.Pin.IN)

def send_message(message):
    """Send a message to the USB serial connection (prints to stdout)."""
    print(message)
    

def receive_message(timeout=0):
    """
    Check for and receive a message from the USB serial connection (stdin).
    Optional timeout (seconds), 0 = non-blocking check.
    """
    if sys.stdin in select.select([sys.stdin], [], [], timeout)[0]:
        return sys.stdin.readline().strip()
    return None
# Simple script to communicate between a pi and a pico
# PICO Script
# open a direct connection over USB
#import machine

#button = machine.Pin(14, machine.Pin.IN)

counter = 1
while True:
    if button.value == 1:        
        send_message(f"From PICO: Button pressed {counter} times")
        utime.sleep(1)
    utime.sleep(0.1)    
        
# while True:
#     if button.value() == 1:
#         print("You pressed the button!")
#         utime.sleep(1)
# while True:
#     message = receive_message()
#     if message:
#         print(f"Received: {message}")
#         if message == "ping":
#             send_message("pong")
#         else:
#             send_message(f"Echo: {message}")
#     utime.sleep(0.1)
        

# Simple script to communicate between a pi and a pico
# PICO Script
# open a direct connection over USB
import sys
import select

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
import time

counter = 0

while True:
    # Send periodic message to Pi
    send_message(f"Hello from Pico, count: {counter}")
    counter += 1

    # Check for incoming message
    message = receive_message(0.1)
    if message:
        send_message(f"Received from Pi: {message}")

    time.sleep(0.5)




        

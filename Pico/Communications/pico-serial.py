import utime
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
# Simple script to communicate between a pi and a pico
# PICO Script
# open a direct connection over USB

while True:
    message = receive_message()
    if message:
        print(f"Received: {message}")
        if message == "ping":
            send_message("pong")
        else:
            send_message(f"Echo: {message}")
    utime.sleep(0.1)
        

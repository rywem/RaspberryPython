# Traffic light game
# https://docs.sunfounder.com/projects/thales-kit/en/latest/micropython/traffic_light.html
import machine
import utime
import _thread

# Define LEDs
led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

# Define button with pull-down resister (no internal pull-down since a 10k ohm external pull down resistor is used)
button = machine.Pin(16, machine.Pin.IN)

global button_status
button_status = 0
lock = _thread.allocate_lock() # thread-safe access to button_status


def button_thread():
    # Thread to monitor the button press and update button_status safely
    global button_status
    while True:
        if button.value() == 1:
            with lock:
                button_status = 1
            utime.sleep_ms(50) #debounce delay
            while button.value() == 1:
                utime.sleep_ms(50) # wait until the button is released

_thread.start_new_thread(button_thread, ())

while True:
    with lock:
        if button_status == 1:
            led_red.value(1)
            utime.sleep(10)
            led_red.value(0)
            
            # reset button status after handling
            button_status = 0
    #global button_status
    #button_status = 0

    led_red.value(1)
    utime.sleep(5)
    led_red.value(0)

    led_yellow.value(1)
    utime.sleep(2)
    led_yellow.value(0)

    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)

    led_yellow.value(1)
    utime.sleep(2)
    led_yellow.value(0)

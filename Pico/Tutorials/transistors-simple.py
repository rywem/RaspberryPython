import machine
button = machine.Pin(14, machine.Pin.IN)
signal = machine.Pin(15, machine.Pin.OUT)

# pressing the button should toggle the LED on and off
while True:
    button_status = button.value()
    if button_status== 1:
        signal.value(1)
    elif button_status == 0:
        signal.value(0)

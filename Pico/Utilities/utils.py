from machine import Pin

# A function to clean up a pin that was previously in use
def pin_cleanup(pin):
    pin.value(0)
    pin.value(Pin.IN)
    print("Pin cleaned")
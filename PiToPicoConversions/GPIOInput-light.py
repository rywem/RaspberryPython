import machine
import utime

pinIn = machine.Pin(15, machine.Pin.IN)
pinLight = machine.Pin(14, machine.Pin.OUT)


while True:
    readVal = pinIn.value()
    if readVal == 0:
        pinLight.value(1)
    else:
        pinLight.value(0)
    print(readVal)
    utime.sleep(1)


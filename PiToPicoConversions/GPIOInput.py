import machine
import utime

pinIn = machine.Pin(15, machine.Pin.IN)



while True:
    readVal = pinIn.value()
    print(readVal)
    utime.sleep(1)


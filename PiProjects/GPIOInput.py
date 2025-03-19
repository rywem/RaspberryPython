# read 3.3v GPIO 1 with GPIO 40
"""
Pull-Up vs. Pull-Down Resistors
--------------------------------
Pull-up and pull-down resistors are used in digital circuits to define a known state 
(HIGH or LOW) for an input pin when no active signal is driving it.

1. Pull-Down Resistor:
   - Ensures that an input pin reads LOW (0V, logic 0) when not actively driven HIGH.
   - Connected between the input pin and GND.
   - When a button is pressed, the input goes HIGH; otherwise, it remains LOW.

   Example Circuit:
       VCC (HIGH) --- Switch --- Input Pin
                        |
                        R (10kΩ)
                        |
                        GND (LOW)

2. Pull-Up Resistor:
   - Ensures that an input pin reads HIGH (VCC, logic 1) when not actively pulled LOW.
   - Connected between the input pin and VCC.
   - When a button is pressed, the input goes LOW; otherwise, it remains HIGH.

   Example Circuit:
       VCC (HIGH)
           |
           R (10kΩ)
           |
       Input Pin --- Switch --- GND (LOW)

Key Differences:
------------------------------------------------------
| Feature          | Pull-Down Resistor | Pull-Up Resistor |
|-----------------|------------------|------------------|
| Default State   | LOW (0V)         | HIGH (VCC)       |
| Connected To    | GND              | VCC              |
| Use Case        | Default LOW, activated HIGH | Default HIGH, activated LOW |
| Example Button  | Press connects to VCC | Press connects to GND |

Pull-ups are more common as many microcontrollers (e.g., Arduino, Raspberry Pi) have internal pull-ups.
"""

import RPi.GPIO as GPIO
from time import sleep
# use the physical numbering system on the board
# instead of BCIM system
GPIO.setmode(GPIO.BOARD)
inPin = 40
GPIO.setup(inPin, GPIO.IN)

try:
    while True:        
        readVal = GPIO.input(inPin) #read the value from the 40
        print(readVal)
        sleep(1)
except KeyboardInterrupt: 
    GPIO.cleanup()
    print("ending...")

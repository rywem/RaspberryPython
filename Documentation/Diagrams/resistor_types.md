# 🧪 Raspberry Pi GPIO Button Configuration: Pull-Up vs Pull-Down

This guide explains how to wire a button to a Raspberry Pi GPIO pin using **pull-up** and **pull-down** resistor configurations.

---

## 🟢 Pull-Up Resistor Configuration

**Behavior:**
- **Button not pressed** → GPIO reads **HIGH**
- **Button pressed** → GPIO reads **LOW**

### 🔌 Circuit Diagram

3.3V | [Button] | GPIO17 ----///---- GND 
    10kΩ
  
\ 3.3V
  |
 [Button]
  |
 GPIO17 ----/\/\/\---- GND
            10kΩ
  
    
### 📖 How It Works

- A 10kΩ resistor pulls GPIO17 **down to GND** by default.
- When the button is pressed, it connects GPIO17 directly to **3.3V**.
- This causes the GPIO to read **HIGH** when pressed.

---

## 🔴 Pull-Down Resistor Configuration

**Behavior:**
- **Button not pressed** → GPIO reads **LOW**
- **Button pressed** → GPIO reads **HIGH**

### 🔌 Circuit Diagram
GND | [Button] | GPIO17 ----///---- 3.3V 10kΩ
 GND
  |
 [Button]
  |
 GPIO17 ----/\/\/\---- 3.3V
            10kΩ


### 📖 How It Works

- A 10kΩ resistor pulls GPIO17 **up to 3.3V** by default.
- When the button is pressed, it connects GPIO17 directly to **GND**.
- This causes the GPIO to read **LOW** when pressed.

---

## 🧠 Using Raspberry Pi's Internal Pull Resistors (Optional)

Instead of using a physical resistor, you can enable the internal pull-up or pull-down resistors in code using Python and the `RPi.GPIO` library.

### ✅ Pull-Up Example

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if GPIO.input(17) == GPIO.LOW:
    print("Button Pressed")

### ✅ Pull-Down Example
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(17) == GPIO.HIGH:
    print("Button Pressed")

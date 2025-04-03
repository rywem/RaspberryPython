# 🧪 GPIO Button Configuration: Pull-Up vs Pull-Down Resistors

This guide shows how to wire a button to a Raspberry Pi GPIO pin using **pull-up** and **pull-down** resistor configurations.

---

## 🟢 Pull-Up Resistor Configuration

**Behavior**:  
- Button *not pressed* ➝ **GPIO reads HIGH**  
- Button *pressed* ➝ **GPIO reads LOW**

### 🔌 Circuit Diagram
3.3V | [Button] | GPIO17 ----///---- GND
    10kΩ


3.3V
  |
[Button]
  |
GPIO17 ----/\/\/\---- GND  
           10kΩ


### 📖 How It Works

- A 10kΩ resistor pulls GPIO17 **down to GND** by default.
- Pressing the button connects GPIO17 to **3.3V**, overriding the pull-down and making the input HIGH.

---

## 🔴 Pull-Down Resistor Configuration

**Behavior**:  
- Button *not pressed* ➝ **GPIO reads LOW**  
- Button *pressed* ➝ **GPIO reads HIGH**

### 🔌 Circuit Diagram

GND | [Button] | GPIO17 ----///---- 3.3V
10kΩ

GND
  |
[Button]
  |
GPIO17 ----/\/\/\---- 3.3V  
           10kΩ



### 📖 How It Works

- A 10kΩ resistor pulls GPIO17 **up to 3.3V** by default.
- Pressing the button connects GPIO17 to **GND**, overriding the pull-up and making the input LOW.

---

## 🧠 Tip: Use Raspberry Pi's Internal Resistors (Optional)

Raspberry Pi GPIO pins support internal pull-up/down resistors. You can enable them via Python using `RPi.GPIO`:

### 🐍 Pull-Up Example

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if GPIO.input(17) == GPIO.LOW:
    print("Button Pressed")


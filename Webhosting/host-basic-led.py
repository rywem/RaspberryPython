from flask import Flask, render_template_string, redirect, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# HTML Template
html = """
<!doctype html>
<title>LED Control</title>
<h1>LED is {{ state }}</h1>
<form action="/on" method="post"><button>Turn ON</button></form>
<form action="/off" method="post"><button>Turn OFF</button></form>
"""

@app.route('/')
def index():
    state = "ON" if GPIO.input(LED_PIN) else "OFF"
    return render_template_string(html, state=state)

@app.route('/on', methods=['POST'])
def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return redirect(url_for('index'))

@app.route('/off', methods=['POST'])
def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return redirect(url_for('index'))

# Clean up GPIO on exit
import atexit
atexit.register(GPIO.cleanup)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

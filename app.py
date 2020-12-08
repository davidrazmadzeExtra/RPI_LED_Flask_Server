import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import datetime
import time
import socket
app = Flask(__name__)

# Configuration variables, feel free to change these.

PORT_NUMBER = 8080
LED = 18

# # # # # GPIO Functions # # # # #


def setupGPIO():
    print('\n[*] Setting up GPIO Pins')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.LOW)


def flashLED(count):
    print('[*] Flashing LED')
    for i in range(count):
        toggleLED("on")
        time.sleep(.1)

        toggleLED("off")
        time.sleep(.1)


def toggleLED(state):
    if state == "on":
        GPIO.output(LED, GPIO.HIGH)
    if state == "off":
        GPIO.output(LED, GPIO.LOW)


# # # # # Helper Functions # # # # #


def printHostIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    print("[*] Raspberry Pi IP Address: " + ip)
    print("[*] Port number " + str(PORT_NUMBER) + "\n")


# # # # # Flask Functions # # # # #


@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%m-%d-%Y %H:%M")
    templateData = {
        'time': timeString
    }
    return render_template('index.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if action == "on":
        toggleLED("on")
    if action == "off":
        toggleLED("off")

    return render_template("index.html")


# # # # # MAIN # # # # #

if __name__ == "__main__":
    setupGPIO()
    flashLED(5)
    printHostIP()
    app.run(host='0.0.0.0', port=PORT_NUMBER, debug=True)

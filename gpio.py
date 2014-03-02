import RPi.GPIO as gpio
import time

sleeptime = 0.1

gpio.setmode(gpio.BCM)

gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.IN)

while True:
    inputvalue = int(gpio.input(23))
    print(inputvalue)
    gpio.output(15, gpio.HIGH)
    gpio.output(18, gpio.LOW)
    time.sleep(sleeptime)
    gpio.output(15, gpio.LOW)
    gpio.output(18, gpio.HIGH)
    time.sleep(sleeptime)
    


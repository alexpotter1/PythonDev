try:
    import RPi.GPIO as gpio
except ImportError:
    print("Update your Raspberry Pi, 'cause the GPIO library isn't installed!")

import time

sleeptime = 0.1

gpio1 = 15
gpio2 = 18
gpio3 = 23

gpio.setmode(gpio.BCM) # uses Broadcom mode for GPIO (recommended)

# setting up the GPIO pins (in this case, GPIO15, GPIO18 and GPIO23 and GND)
gpio.setup(gpio1, gpio.OUT)
gpio.setup(gpio2, gpio.OUT)
gpio.setup(gpio3, gpio.IN) # input setup code for a button that doesn't work yet

# simple LED flashing program
while True:
    inputvalue = int(gpio.input(gpio3)) # some code for a button that doesn't work yet
    print(inputvalue) # same

    gpio.output(gpio1, gpio.HIGH) # sets GPIO15 to ON (LED lights up)
    gpio.output(gpio2, gpio.LOW) # GPIO18 OFF (second LED is off)
    time.sleep(sleeptime) # waits for 'sleeptime' seconds
    gpio.output(gpio1, gpio.LOW) # sets GPIO15 (first LED) to OFF
    gpio.output(gpio2, gpio.HIGH) # sets GPIO18 (second LED) to ON
    time.sleep(sleeptime) # waits sleeptime, then restarts
    


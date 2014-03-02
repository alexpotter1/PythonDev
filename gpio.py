try:
    import RPi.GPIO as gpio
except ImportError:
    print("Update your Raspberry Pi, 'cause the GPIO library isn't installed!")

import time

sleeptime = 0.1

gpio.setmode(gpio.BCM) # uses Broadcom mode for GPIO (recommended)

# setting up the GPIO pins (in this case, GPIO15, GPIO18 and GPIO23 and GND)
gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.IN) # input setup code for a button that doesn't work yet

# simple LED flashing program
while True:
    inputvalue = int(gpio.input(23)) # some code for a button that doesn't work yet
    print(inputvalue) # same

    gpio.output(15, gpio.HIGH) # sets GPIO15 to ON (LED lights up)
    gpio.output(18, gpio.LOW) # GPIO18 OFF (second LED is off)
    time.sleep(sleeptime) # waits for 'sleeptime' seconds
    gpio.output(15, gpio.LOW) # sets GPIO15 (first LED) to OFF
    gpio.output(18, gpio.HIGH) # sets GPIO18 (second LED) to ON
    time.sleep(sleeptime) # waits sleeptime, then restarts
    


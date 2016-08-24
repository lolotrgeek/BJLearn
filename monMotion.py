#!/usr/bin/env python
 
import sys
import time
import RPi.GPIO as io
import subprocess
 
io.setmode(io.BCM)
SHUTOFF_DELAY = 60  # seconds
PIR_PIN = 1         # The PIN the sensor is connected to
 
def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
 
    while True:
        if io.input(PIR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() &amp;amp;amp;gt; (last_motion_time + SHUTOFF_DELAY):
                turned_off = True
                turn_off()
        time.sleep(.1)
 
def turn_on():
    subprocess.call(&amp;amp;amp;quot;sh /home/pi/Documents/PIR/monitor_on.sh&amp;amp;amp;quot;, shell=True)
 
def turn_off():
    subprocess.call(&amp;amp;amp;quot;sh /home/pi/Documents/PIR/monitor_off.sh&amp;amp;amp;quot;, shell=True)
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()

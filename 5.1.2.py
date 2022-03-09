#blink LED  /home/pi
import RPi.GPIO as GPIO
import time 
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM)   #GPTO18
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
while True:
    GPIO.output(18,1)
    GPIO.output(23,1)
    GPIO.output(24,1)
    break

#cleanup
GPIO.cleanup()
print("program executed")
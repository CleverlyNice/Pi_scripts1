#blink LED  /home/pi
import RPi.GPIO as GPIO
import time 
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM)   #GPTO18

#blinking function
def blink(pin):
    #setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

#main program blink GPIO18(pin12) 10 times
while True:
    blink(18)

#cleanup
GPIO.cleanup()
print("program executed")
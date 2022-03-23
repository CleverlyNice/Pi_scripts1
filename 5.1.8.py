import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)   

def fade(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(1)
    GPIO.output(pin, 0.75)
    time.sleep(1)

for i in range(0,10):
    fade(18) 
    fade(23)

#cleanup
GPIO.cleanup()
print("program executed")
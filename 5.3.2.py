import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)   
GPIO.setup(17,GPIO.IN)

def light(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

while True:
    if (GPIO.input(17)== 0):
        light(18)
        print("light on")
        time.sleep(0.5)
    else:
        print("light off")
        time.sleep(0.5)

GPIO.cleanup()
print("program executed")
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)   
GPIO.setup(17,GPIO.IN)
GPIO.setup(12,GPIO.IN)

while True:
    if (GPIO.input(17)== 0) or (GPIO.input(12)== 0):
        GPIO.output(18, 1)
        print("light on")
        time.sleep(0.5)
    else:
        GPIO.output(18, 0)
        print("light off")
        time.sleep(0.5)

GPIO.cleanup()
print("program executed")
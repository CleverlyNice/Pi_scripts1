import RPi.GPIO as GPIO
import time 
import datetime

GPIO.setmode(GPIO.BCM) 
GPIO.setup (17, GPIO.OUT)
GPIO.setup (18, GPIO.IN)

while True:

    GPIO.output (17, 1)
    time.sleep (0.00001)
    GPIO.output (17, 0)
    while (GPIO.input(18)==0):

        pass
    
    
    signalhigh = datetime.datetime.now()
    
    while (GPIO.input(18)==1):
        pass

    
    signallow = datetime.datetime.now()

    timepassed = signallow - signalhigh
    distance = timepassed.total_seconds()*17000
    print(distance)
    time.sleep(0.5)

#blink LED  /home/pi
import RPi.GPIO as GPIO
import time 
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM)   #GPTO18
GPIO.setup(17,GPIO.IN)

#blinking function
def shot_pulse(pin):
    #setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

def long_pulse(pin):
    #setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(1.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)


#main program blink GPIO18(pin12) 10 times

for i in range(0,10):
    if (GPIO.input(17)== 0):
        shot_pulse(18)
        long_pulse(18)     
        shot_pulse(18)

#cleanup
GPIO.cleanup()
print("program executed")
#blink LED  /home/pi
import RPi.GPIO as GPIO
import time 
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM)   #GPTO18
GPIO.setup(17,GPIO.IN)
#blinking function
def blink(pin):
    #setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    time.sleep(0.5)
    GPIO.output(pin, 1)
    time.sleep(0.5)

for i in range(10):
    blink(18)
while True:
    if (GPIO.input(17)== 0):
        print("blinking")
        blink (23)
        time.sleep(0.3)
    else:
        print("not blinking")
        time.sleep(0.3)
#cleanup
GPIO.cleanup()
print("program executed")

#!/usr/bin/env python3 
import cgitb ; cgitb.enable() 
import spidev 
import time
import busio
import digitalio
import board
import requests
from adafruit_bus_device.spi_device import SPIDevice
url = "http://jeffrey.hub.ubeac.io/iotessjeffrey"
uid = "iotessjeffrey"
 
# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize control pins for adc
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select CE0 for adc
adc = SPIDevice(spi, cs0, baudrate= 1000000)

# read SPI data 8 possible adc's (0 thru 7) 
def readadc(adcnum): 
	if ((adcnum > 7) or (adcnum < 0)): 
		return -1 
	with adc:
		r = bytearray(3)
		spi.write_readinto([1,(8+adcnum)<<4,0], r)
		time.sleep(0.000005)
		adcout = ((r[1]&3) << 8) + r[2] 
		return adcout 
 
while True:
	tmp0 = readadc(1) # read channel 0 
	#print ("input0:",tmp0)
	data= {
		"id": uid,
		"sensors":[{
			'id': 'adc kanaal0',
			'data': tmp0
			}]
		}
	r = requests.post(url, verify=False,  json=data)
	print((500*tmp0)/1023)
	time.sleep(1)


#!/usr/bin/python
import spidev
import time 
import RPi.GPIO as GPIO
import speaker.py as speaker

 
#Initializing the ports and maximum speed (Hz) for the for the spidev IR sensor object. 
spi = initializeSpiDevObject()

GPIO = speaker.initializeSpeakerGPIO()
speakerPin = speaker.initializeSpeakerPin()



 
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data

def initializeSpiDevObject():
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz=1000000
    return spi

# https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/
# spidev libraries may not work properly, see above link for solutions
if __name__ == "__main__":
  while True:
    v=(readChannel(0)/1023.0)*3.3
    dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439
    print("Distanz: %.2f cm" % dist)
    if dist < 25:
        speaker.speaker_object_detected_basic()
    time.sleep(2)

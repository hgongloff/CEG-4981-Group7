#!/usr/bin/python
import spidev
import time 


class DistanceSensor:

  def __init__(self):
    self.spi = spidev.SpiDev()
    self.spi.open(0,0)
    self.spi.max_speed_hz=1000000
 
 
  def readChannel(self, channel):
    val = self.spi.xfer2([1,(8+channel)<<4,0])
    data = ((val[1]&3) << 8) + val[2]
    return data

  def get_distance(self):
    while True:
      v=(self.readChannel(0)/1023.0)*3.3
      dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439
      print("Distanz: %.2f cm" % dist)
      time.sleep(2)
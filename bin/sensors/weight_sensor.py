import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711


class WeightSensor:

    def __init__(self):
        self.hx = HX711(6, 5)
        self.hx.set_offset(9049133.5625)
        self.hx.set_scale(456.48)

    def get_weight(self):
        try:
            self.hx.power_up()
            time.sleep(2)
            val = self.hx.get_grams()
            print(val)

            self.hx.power_down()
            time.sleep(.001)
            # self.hx.power_up()

            # time.sleep(2)
            return val
        except (KeyboardInterrupt, SystemExit):
            self.cleanAndExit()
        return 


    def cleanAndExit(self):
        print("Cleaning...")
        GPIO.cleanup()
        print("Bye!")
        sys.exit()


    def setup(self):
        """
        code run once
        """
        self.hx.set_offset(9051810.5)
        self.hx.set_scale(457.2)


    def loop(self):
        """
        code run continuosly
        """

        try:
            self.val = self.hx.get_grams()
            print(val)

            self.hx.power_down()
            time.sleep(.001)
            self.hx.power_up()

            time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            self.cleanAndExit()




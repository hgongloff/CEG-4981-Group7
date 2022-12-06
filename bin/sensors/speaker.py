import RPi.GPIO as GPIO
from time import sleep
import threading

class Speaker:

    def __init__(self):
        self.pin = GPIO.PWM(7, 100)
        self.run_thread = threading.Thread(target=self.play_alarm, args=(1,))
        #self.pin.start(50)

    def play_alarm(self, name):
        print(name)
        self.pin.start(50)
        GPIO.output(7, GPIO.HIGH)
        self.pin.ChangeFrequency(16.35) # C0
        sleep(1)
        self.pin.ChangeFrequency(261.63) # C4
        sleep(1)
        self.pin.ChangeFrequency(293.66) # D4
        sleep(1)
        self.pin.ChangeFrequency(329.63) # E4
        sleep(1)
        self.pin.ChangeFrequency(349.23) # F4
        sleep(1)
        self.pin.ChangeFrequency(392.00) # G4
        sleep(1)
        self.pin.ChangeFrequency(440.00) # A4
        sleep(1)
        self.pin.ChangeFrequency(493.88) # B4
        sleep(1)
        self.pin.ChangeFrequency(523.25) # A5
        sleep(1.5)
        self.pin.ChangeFrequency(16.35) # C0
        sleep(1)
        GPIO.output(7, GPIO.LOW)
        sleep(1)
        self.pin.stop()

    def stop_thread(self):
        print("stop thread")
        self.run_thread.join()
        print("thread stopped")
        return


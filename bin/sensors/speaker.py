import RPi.GPIO as GPIO
from time import sleep

class Speaker:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        pin23 = GPIO.PWM(23, 100)
        pin23.start(50)

    def play_alarm(self):
        GPIO.output(23, GPIO.HIGH)
        pin23.ChangeFrequency(16.35) # C0
        sleep(1)
        pin23.ChangeFrequency(261.63) # C4
        sleep(1)
        pin23.ChangeFrequency(293.66) # D4
        sleep(1)
        pin23.ChangeFrequency(329.63) # E4
        sleep(1)
        pin23.ChangeFrequency(349.23) # F4
        sleep(1)
        pin23.ChangeFrequency(392.00) # G4
        sleep(1)
        pin23.ChangeFrequency(440.00) # A4
        sleep(1)
        pin23.ChangeFrequency(493.88) # B4
        sleep(1)
        pin23.ChangeFrequency(523.25) # A5
        sleep(1.5)
        pin23.ChangeFrequency(16.35) # C0
        sleep(1)
        GPIO.output(23, GPIO.LOW)
        sleep(1)


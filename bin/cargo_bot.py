from sensors.speaker import Speaker
from cargo_bot_ble import CargoBotBle
import RPi.GPIO as GPIO


class CargoBot:
    def __init__(self):
        self.speaker = Speaker(pin=GPIO.PWM(23, 100))
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        pin23 = GPIO.PWM(23, 100)
        pin23.start(50)
        self.cargo_ble = CargoBotBle()

    def play_alarm(self):
        self.speaker.play_alarm()

    def connect_to_phone(self):
        print("Connecting to mobile device")
        self.cargo_ble.run_thread.start()

    def send_message(self):
        print("Sending message to mobile device")
        # self.cargo_ble.send_message()

    def get_message(self):
        print("Getting message from mobile device")
        # self.cargo_ble.get_message()

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def __str__(self):
        return "CargoBot: " + str(self.cargo)

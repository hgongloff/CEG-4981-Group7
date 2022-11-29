from sensors.speaker import Speaker
from cargo_bot_ble import CargoBotBle
from sensors.weight_sensor import WeightSensor
from sensors.distance_sensor import DistanceSensor
from sensors.camera import Camera
import RPi.GPIO as GPIO
import threading


class CargoBot:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        self.speaker = Speaker()
        self.weight_sensor = WeightSensor()
        self.cargo_ble = CargoBotBle()
        self.distance_senor = DistanceSensor()
        self.camera = Camera()

    def play_alarm(self):
        self.speaker.run_thread.start()
        print("Number of threads: " + str(threading.active_count()))

    def connect_to_phone(self):
        print("Connecting to mobile device")
        self.cargo_ble.run_thread.start()

    def send_message(self):
        print("Sending message to mobile device")
        try:
            self.cargo_ble.write_value('Hello World!', [])
        except Exception as ex:
            print("Error sending message to mobile device")
            print(ex)
            pass

    def get_message(self):
        print("Getting message from mobile device")
        # self.cargo_ble.get_message()

    def get_weight(self):
        setattr(self.cargo_ble, 'current_weight', 12)
        return self.weight_sensor.get_weight()

    def get_cargo(self):
        return self.cargo

    def get_distance(self):
        return self.distance_senor.get_distance()

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_picture(self):
        self.camera.take_picture()
    
    def stop_threads(self):
        self.speaker.stop_thread()
        self.cargo_ble.stop_thread()
        #self.weight_sensor.stop_thread()
        return

    def __str__(self):
        return "CargoBot: " + str(self.cargo)

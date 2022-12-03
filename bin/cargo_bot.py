from sensors.speaker import Speaker
from cargo_bot_ble import CargoBotBle
from sensors.weight_sensor import WeightSensor
from sensors.distance_sensor import DistanceSensor
from sensors.camera import Camera
import RPi.GPIO as GPIO
import threading
import time
from sensors.motor import Motor


class CargoBot:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(31, GPIO.OUT)
        self.speaker = Speaker()
        self.weight_sensor = WeightSensor()
        self.cargo_ble = CargoBotBle()
        self.motor = Motor()
        self.get_command_thread = threading.Thread(target=self.get_command)
        #self.distance_senor = DistanceSensor()
        #self.camera = Camera()
        self.get_command_thread.start()

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
        self.stop_thread()
        #self.weight_sensor.stop_thread()
        return

    def get_command(self):
        while True:
            command = self.cargo_ble.current_command
            if (command == 'Go'):
                print("Go")
                self.motor.forward_thread.start()
                self.motor.forward_thread.join()
                self.motor.forward_thread = threading.Thread(target=self.motor.move_forward,  args=(1,))
                command = ""
                self.cargo_ble.current_command = ""
            elif (command == 'Stop'):
                print("Stop")
                self.motor.stop_moving()
                command = ""
                self.cargo_ble.current_command = ""
            elif (command == 'Alarm'):
                print("Alarm")
                command = ""
                self.cargo_ble.current_command = ""
            elif (command == 'Back'):
                print("Back")
                self.motor.backward_thread.start()
                self.motor.backward_thread.join()
                self.motor.backward_thread = threading.Thread(target=self.motor.move_backward,  args=(1,))
                command = ""
                self.cargo_ble.current_command = ""
            elif (command == 'Left'):
                print("Left")
                self.motor.left_thread.start()
                self.motor.left_thread.join()
                self.motor.left_thread = threading.Thread(target=self.motor.move_left,  args=(1,))
                command = ""
                self.cargo_ble.current_command = ""
            elif (command == 'Right'):
                print("Right")
                self.motor.right_thread.start()
                self.motor.right_thread.join()
                self.motor.right_thread = threading.Thread(target=self.motor.move_right,  args=(1,))
                command = ""
                self.cargo_ble.current_command = ""
            time.sleep(0.1)

    def stop_thread(self):
        print("stop thread")
        self.run_thread.join()
        print("thread stopped")
        return

    def __str__(self):
        return "CargoBot: " + str(self.cargo)

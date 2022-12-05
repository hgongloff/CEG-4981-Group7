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
        self.current_thread = ""
        self.command_thread_map = {'forward': self.motor.forward_thread, 'backward': self.motor.backward_thread, 'left': self.motor.left_thread, 'right': self.motor.right_thread, 'go': self.motor.go_thread}
        self.command_map = {'forward': self.motor.move_forward, 'backward': self.motor.move_backward, 'left': self.motor.move_left, 'right': self.motor.move_right, 'go': self.motor.go}

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
            if self.motor.thread_finished:
                self.motor.thread_finished = False
                self.motor.thread_running = False
                print("thread finished")
                print(self.current_thread)
                self.command_thread_map[self.current_thread].join()
                self.command_thread_map[self.current_thread] = threading.Thread(target=self.command_map[self.current_thread],  args=(1,))
                self.current_thread = ""

            command = self.cargo_ble.current_command
            if (command == 'Forward'):
                print("Forward")
                if self.current_thread == "":
                    self.current_thread = "forward"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started forward thread")
                    command = ""
                    self.cargo_ble.current_command = ""
                elif self.current_thread == "forward": 
                    print("thread already running")
                else:
                    print("thread already running")
                    self.motor.thread_running = False
                    self.motor.thread_finished = False
                    self.command_thread_map[self.current_thread].join()
                    self.command_thread_map[self.current_thread] = threading.Thread(target=self.command_map[self.current_thread],  args=(1,))
                    self.current_thread = "forward"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started forward thread")
                    command = ""
                    self.cargo_ble.current_command = ""

            elif (command == 'Stop') and self.motor.thread_running:
                print("Stop Command")
                self.motor.thread_running = False
                self.motor.thread_finished = True
                command = ""
                self.cargo_ble.current_command = ""
            elif (command == 'Alarm'):
                print("Alarm")
                command = ""
                self.cargo_ble.current_command = ""
            elif (command == 'Back'):
                print("Back")
                if self.current_thread == "":
                    self.current_thread = "backward"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started backward thread")
                    command = ""
                    self.cargo_ble.current_command = ""
                elif self.current_thread == "backward":
                    print("thread already running")
                else:
                    print("thread already running")
                    self.motor.thread_running = False
                    self.motor.thread_finished = False
                    self.command_thread_map[self.current_thread].join()
                    self.command_thread_map[self.current_thread] = threading.Thread(target=self.command_map[self.current_thread],  args=(1,))
                    self.current_thread = "backward"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started backward thread")
                    command = ""
                    self.cargo_ble.current_command = ""
            elif (command == 'Left'):
                print("Left")
                if self.current_thread == "":
                    self.current_thread = "left"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started left thread")
                    command = ""
                    self.cargo_ble.current_command = ""
                elif self.current_thread == "left":
                    print("thread already running")
                else:
                    print("thread already running")
                    self.motor.thread_running = False
                    self.motor.thread_finished = False
                    self.command_thread_map[self.current_thread].join()
                    self.command_thread_map[self.current_thread] = threading.Thread(target=self.command_map[self.current_thread],  args=(1,))
                    self.current_thread = "left"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started left thread")
                    command = ""
                    self.cargo_ble.current_command = ""
            elif (command == 'Right'):
                if self.current_thread == "":
                    print("Right")
                    self.current_thread = "right"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started right thread")
                    command = ""
                    self.cargo_ble.current_command = ""
                elif self.current_thread == "right":
                    print("thread already running")
                else:
                    print("thread already running")
                    self.motor.thread_running = False
                    self.motor.thread_finished = False
                    self.command_thread_map[self.current_thread].join()
                    self.command_thread_map[self.current_thread] = threading.Thread(target=self.command_map[self.current_thread],  args=(1,))
                    self.current_thread = "right"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started right thread")
                    command = ""
                    self.cargo_ble.current_command = ""
            elif "Speed" in command:
                print(f"New Speed = {command.split(' ')[1]}")
                new_speed = command.split(" ")[1]
                new_speed = int(new_speed)
                if new_speed > 100:
                    new_speed = 100
                elif new_speed < 0:
                    new_speed = 0
                self.motor.speed = new_speed
                command = ""
                self.cargo_ble.current_command = ""
            elif "Go" in command:
                if self.current_thread == "":
                    print("Go")
                    self.current_thread = "go"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started go thread")
                    command = ""
                    self.cargo_ble.current_command = ""
                elif self.current_thread == "go":
                    print("thread already running")
                else:
                    print("thread already running")
                    self.motor.thread_running = False
                    self.motor.thread_finished = False
                    self.command_thread_map[self.current_thread].join()
                    self.command_thread_map[self.current_thread] = threading.Thread(target=self.command_map[self.current_thread],  args=(1,))
                    self.current_thread = "go"
                    self.motor.thread_running = True
                    self.command_thread_map[self.current_thread].start()
                    print("started go thread")
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

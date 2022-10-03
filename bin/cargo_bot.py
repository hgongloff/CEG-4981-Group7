from sensors.speaker import Speaker
from cargo_bot_ble import CargoBotBle


class CargoBot:
    def __init__(self):
        self.speaker = Speaker()
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

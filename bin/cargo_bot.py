from sensors.speaker import Speaker
from cargo_bot_ble import CargoBotBle


class CargoBot:
    def __init__(self):
        self.speaker = Speaker()
        self.cargo_ble = CargoBotBle()

    def play_alarm(self):
        self.speaker.play_alarm()

    def connect_to_phone(self):
        self.cargo_ble.connect()

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def __str__(self):
        return "CargoBot: " + str(self.cargo)

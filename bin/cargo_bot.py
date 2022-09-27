

class CargoBot:
    def __init__(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def __str__(self):
        return "CargoBot: " + str(self.cargo)

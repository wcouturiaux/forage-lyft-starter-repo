from abc import ABC


class ITires(ABC):
    def needs_service(self):
        pass


class OctoprimeTires(ITires):
    def __init__(self, tire_wear: [4]):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3.0

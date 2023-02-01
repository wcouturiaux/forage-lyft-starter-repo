from abc import ABC, abstractmethod


class IBattery(ABC):
    def needs_service(self):
        pass


class IEngine(ABC):
    def needs_service(self):
        pass


# ENGINES
class CapuletEngine(IEngine):

    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000


class WilloughbyEngine(IEngine):

    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000


class SternmanEngine(IEngine):

    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on

# Batteries


class SpindlerBattery(IBattery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year >= 3


class NubbinBattery(IBattery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year >= 4

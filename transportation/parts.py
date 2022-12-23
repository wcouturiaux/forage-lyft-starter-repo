from abc import ABC, abstractmethod


class IBattery(ABC):
    def needs_service(self):
        pass


class IEngine(ABC):
    def needs_service(self):
        pass

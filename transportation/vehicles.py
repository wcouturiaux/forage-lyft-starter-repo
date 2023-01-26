from abc import ABC, abstractmethod


class IServiceable(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class Car(IServiceable):

    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass

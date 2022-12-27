from abc import ABC, abstractmethod


class IServiceable(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class Car(IServiceable):

    def __init__(self, last_service_date, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass

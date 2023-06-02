from abc import ABC, abstractmethod


class Tire(ABC):

    def __init__(self, tire_wear_numbers):
        self.tire_wear_numbers = tire_wear_numbers

    @abstractmethod
    def needs_service(self):
        pass
from car import Car

from battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine


class Glissade(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

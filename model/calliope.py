from car import Car

from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))
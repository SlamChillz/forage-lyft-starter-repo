from car import Car

from battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine


class Rorschach(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
    
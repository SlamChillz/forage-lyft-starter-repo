from car import Car

from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine


class Thovex(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
    
from car import Car

from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from tire.octoprime_tire import OctoprimeTire


class Thovex(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        capulateEngine = CapuletEngine(current_mileage, last_service_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        octoprimeTire = OctoprimeTire(tire_wear_numbers)
        super().__init__(capulateEngine, nubbinBattery, octoprimeTire)

from car import Car

from battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine
from tire.octoprime_tire import OctoprimeTire


class Glissade(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        octoprimeTire = OctoprimeTire(tire_wear_numbers)
        super().__init__(willoughbyEngine, spindlerBattery, octoprimeTire)

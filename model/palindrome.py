from car import Car

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from tire.octoprime_tire import OctoprimeTire


class Palindrome(Car):
    def __init__(self, current_date, last_service_date, warning_light_on, tire_wear_numbers):
        sternmanEngine = SternmanEngine(warning_light_on)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        octoprimeTire = OctoprimeTire(tire_wear_numbers)
        super().__init__(sternmanEngine, spindlerBattery, octoprimeTire)

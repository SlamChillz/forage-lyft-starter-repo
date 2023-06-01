from car import Car

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, current_date, last_service_date, warning_light_on):
        super().__init__(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

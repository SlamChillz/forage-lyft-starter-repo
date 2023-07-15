from car import Car

from battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire


class Rorschach(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        carriganTire = CarriganTire(tire_wear_numbers)
        super().__init__(willoughbyEngine, nubbinBattery, carriganTire)

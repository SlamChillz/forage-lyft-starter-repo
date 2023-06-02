from car import Car

from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire


class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear_numbers))
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_numbers):
        return Palindrome(current_date, last_service_date, warning_light_on, tire_wear_numbers)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers):
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)

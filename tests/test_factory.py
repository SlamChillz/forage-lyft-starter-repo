import unittest
from datetime import datetime

from factory import CarFactory
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex


class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 65000
        last_service_mileage = 0
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.3]
        calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)
        self.assertTrue(isinstance(calliope, Calliope))

    def test_create_glissade(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 65000
        last_service_mileage = 0
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.3]
        glissade = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)
        self.assertTrue(isinstance(glissade, Glissade))

    def test_create_palindrome(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_on = True
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.3]
        palindrome = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_numbers)
        self.assertTrue(isinstance(palindrome, Palindrome))

    def test_create_rorschach(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 65000
        last_service_mileage = 0
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.3]
        rorschach = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)
        self.assertTrue(isinstance(rorschach, Rorschach))

    def test_create_thovex(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 65000
        last_service_mileage = 0
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.3]
        thovex = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_numbers)
        self.assertTrue(isinstance(thovex, Thovex))

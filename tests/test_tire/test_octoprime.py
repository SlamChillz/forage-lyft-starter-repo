import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_carrigan_tire_should_be_serviced(self):
        tire_wear_numbers = [1, 0.8, 0.5, 0.9]

        tire = OctoprimeTire(tire_wear_numbers)
        self.assertTrue(tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.3]

        tire = OctoprimeTire(tire_wear_numbers)
        self.assertFalse(tire.needs_service())

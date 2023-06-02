import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_should_be_serviced(self):
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.9]

        tire = CarriganTire(tire_wear_numbers)
        self.assertTrue(tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        tire_wear_numbers = [0.1, 0.4, 0.5, 0.3]

        tire = CarriganTire(tire_wear_numbers)
        self.assertFalse(tire.needs_service())

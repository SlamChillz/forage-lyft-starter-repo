import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2023-06-02")
        # last_service_date = date.fromisoformat("2021-05-01")
        last_service_date = date.fromisoformat("2020-05-01")

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2023-06-02")
        last_service_date = date.fromisoformat("2022-05-01")

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

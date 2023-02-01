import unittest
from datetime import date

from transportation.parts import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2019-07-01")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue((battery.needs_service()))

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2021-05-01")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse((battery.needs_service()))

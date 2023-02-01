import unittest
from datetime import date

from transportation.parts import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2019-01-01")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue((battery.needs_service()))

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2021-01-01")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse((battery.needs_service()))

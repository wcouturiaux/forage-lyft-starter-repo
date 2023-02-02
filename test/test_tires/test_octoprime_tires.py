import unittest

from transportation.tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1.0, 0.5, 0.7, 0.9]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [1.0, 0.5, 0.5, 0.9]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())

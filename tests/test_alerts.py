import unittest

from brezyweather.alerts import wind_alert


class TestAlerts(unittest.TestCase):
    def test_calm(self):
        self.assertIsNone(wind_alert(20))

    def test_warning_starts_at_threshold(self):
        self.assertEqual(wind_alert(60), "wind-warning")

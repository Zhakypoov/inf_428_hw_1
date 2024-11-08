import math
import unittest


def time_to_cyclic_features(time):
    """
    Convert a time value in hours (0 to 24) to cyclic features using sine and cosine.
    This transformation handles the cyclical nature of time (e.g., 23:00 to 01:00 should have a small difference).

    :param time: Time value in hours (0-24).
    :return: Tuple (sin(time), cos(time)) representing the cyclic features.
    """
    if time < 0 or time >= 24:
        raise ValueError("Time must be between 0 and 24 hours.")

    sin_t = math.sin(2 * math.pi * time / 24)
    cos_t = math.cos(2 * math.pi * time / 24)

    return sin_t, cos_t


class TestTimeTransformation(unittest.TestCase):

    def test_time_to_cyclic_features(self):
        # Test some known times and their expected cyclic transformations
        self.assertEqual(time_to_cyclic_features(0), (0.0, 1.0))  # 0:00
        self.assertEqual(time_to_cyclic_features(6), (1.0, 0.0))  # 6:00
        self.assertEqual(time_to_cyclic_features(12), (0.0, -1.0))  # 12:00
        self.assertEqual(time_to_cyclic_features(18), (-1.0, 0.0))  # 18:00
        self.assertEqual(time_to_cyclic_features(23), (-0.956, -0.292))  # 23:00

    def test_cyclic_difference(self):
        # Testing the difference between two time points (e.g., 23:00 and 01:00)
        time1 = 23
        time2 = 1
        sin1, cos1 = time_to_cyclic_features(time1)
        sin2, cos2 = time_to_cyclic_features(time2)


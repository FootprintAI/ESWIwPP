import unittest

from sensor_loader import SensorLoader

class TestSensorLoader(unittest.TestCase):

    def test_one(self):
        sl = SensorLoader()
        #pd = sl.load_devices()
        #pd = sl.load_devices_geo()
        pd = sl.load_sensors()
        print(pd)

if __name__ == '__main__':
    unittest.main()

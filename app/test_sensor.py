import unittest
from unittest.mock import patch, MagicMock
from sensor import MPL115A2

class TestMPL115A2(unittest.TestCase):

    @patch('smbus2.SMBus')
    def setUp(self, MockSMBus):
        self.mock_bus = MagicMock()
        MockSMBus.return_value = self.mock_bus

        self.sensor = MPL115A2(bus=1, address=0x60)

    def test_read_coefficients(self):
        pass

    def test_get_pressure_temperature(self):
        pass

if __name__ == '__main__':
    unittest.main()

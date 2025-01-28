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
        #Liste de valeurs brutes, représentant les coefficients stockés dans le capteur.
        self.mock_bus.read_i2c_block_data.return_value = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]

        self.sensor.read_coefficients()
        self.mock_bus.read_i2c_block_data.assert_called_with(self.sensor.address, 0x04, 8)

    def test_get_pressure_temperature(self):
        pass

if __name__ == '__main__':
    unittest.main()

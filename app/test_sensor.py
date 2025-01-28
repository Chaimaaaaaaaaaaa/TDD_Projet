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
        self.mock_bus.read_i2c_block_data.return_value = [0x10, 0x20, 0x30, 0x40]

        #Valeurs choisies arbitrairement pour valider les algorithmes et les calculs
        self.sensor.a0 = 1013.25
        self.sensor.b1 = 0.0025
        self.sensor.b2 = -0.0031
        self.sensor.c12 = 0.00017

        self.sensor.get_pressure_temperature()

        self.mock_bus.read_i2c_block_data.assert_called_with(self.sensor.address, 0x00, 4)

if __name__ == '__main__':
    unittest.main()

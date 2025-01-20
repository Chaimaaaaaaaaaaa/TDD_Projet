import unittest
from unittest.mock import patch
from sensor import MPL115A2

class TestMPL115A2(unittest.TestCase):
    @patch('smbus2.SMBus')
    def test_start_conversion(self, MockSMBus):
        mock_bus = MockSMBus.return_value
        sensor = MPL115A2()
        sensor.start_conversion()
        mock_bus.write_byte_data.assert_called_with(0x60, 0x12, 0x00)

    @patch('smbus2.SMBus')
    def test_read_data(self, MockSMBus):
        mock_bus = MockSMBus.return_value

        mock_bus.read_word_data.side_effect = [
            0x8000,
            0x4000
        ]

        sensor = MPL115A2()
        data = sensor.read_data()

        self.assertEqual(data['pressure'], 0x0080)
        self.assertEqual(data['temperature'], 0x0040)

    @patch('smbus2.SMBus')
    def test_write_register(self, MockSMBus):

        register = 0x12
        value = 0x55
        sensor.write_register(register, value)

if __name__ == '__main__':
    unittest.main()
import unittest
from gpio import GPIO

class TestGPIO(unittest.TestCase):
    def test_gpio_init(self):
        gpio = GPIO(1)
        self.assertEqual(gpio.num, 1)
        self.assertEqual(gpio.mode, None)
        self.assertEqual(gpio.value, None)

if __name__ == '__main__':
    unittest.main()
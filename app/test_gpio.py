"""Tests classe GPIO"""

import unittest
from gpio import GPIO

class TestGPIO(unittest.TestCase):
    """Tests pour la classe GPIO"""
    def test_gpio_init(self):
        """Test du constructeur de la classe GPIO"""
        gpio = GPIO(1)
        self.assertEqual(gpio.num, 1)
        self.assertEqual(gpio.mode, None)
        self.assertEqual(gpio.value, None)

    def test_gpio_setmode_getmode(self):
        """Test des methodes setmode et getmode de la classe GPIO"""
        gpio = GPIO(1)
        gpio.setmode("output")
        self.assertEqual(gpio.mode, "output")
        gpio.setmode("input")
        self.assertEqual(gpio.mode, "input")
        with self.assertRaises(ValueError):
            gpio.setmode("hello")

        gpio.setmode("output")
        self.assertEqual(gpio.getmode(), "output")

    def test_gpio_write_read(self):
        """Test des methodes write et read de la classe GPIO"""
        gpio = GPIO(1)
        gpio.setmode("output")
        gpio.write(1)
        self.assertEqual(gpio.value, 1)

        gpio_1 = GPIO(2)
        gpio_1.setmode("input")
        gpio_1.value = 10
        self.assertEqual(gpio_1.read(), 10)

        gpio_in = GPIO(3)
        gpio_in.setmode("input")
        with self.assertRaises(ValueError):
            gpio_in.write(1)

        gpio_out = GPIO(4)
        gpio_out.setmode("output")
        with self.assertRaises(ValueError):
            gpio_out.read()


if __name__ == '__main__':
    unittest.main()

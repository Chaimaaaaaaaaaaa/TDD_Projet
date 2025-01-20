import unittest
from gpio import GPIO

class TestGPIO(unittest.TestCase):
    def test_gpio_init(self):
        gpio = GPIO(1)
        self.assertEqual(gpio.num, 1)
        self.assertEqual(gpio.mode, None)
        self.assertEqual(gpio.value, None)
    
    def test_gpio_setmode(self):
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
        gpio = GPIO(1)
        gpio.write(1)
        self.assertEqual(gpio.value, 1)
        self.assertEqual(gpio.read(), 1)
        

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import MagicMock, patch
from serverGPIO2 import app, pins

class TestServerGPIO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.pins = pins

    def setUp(self):
        """Reset mock GPIO instances before each test."""
        for pin in self.pins:
            self.pins[pin]['gpio'].setmode = MagicMock()
            self.pins[pin]['gpio'].write = MagicMock()
            self.pins[pin]['gpio'].read = MagicMock()
            self.pins[pin]['gpio'].getmode = MagicMock()

    def test_main_page_status(self):
        """Test if the main page loads successfully."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        for pin in self.pins:
            self.assertIn(f"GPIO {pin}".encode(), response.data)

    def test_turn_on_pin(self):
        """Test turning a GPIO pin on."""
        response = self.app.get('/23/on')
        self.assertEqual(response.status_code, 200)
        self.pins[23]['gpio'].write.assert_called_with(1)
        self.assertIn(b"Turned GPIO 23 on.", response.data)

    def test_turn_off_pin(self):
        """Test turning a GPIO pin off."""
        response = self.app.get('/23/off')
        self.assertEqual(response.status_code, 200)
        self.pins[23]['gpio'].write.assert_called_with(0)
        self.assertIn(b"Turned GPIO 23 off.", response.data)

    def test_invalid_pin(self):
        """Test handling an invalid pin."""
        response = self.app.get('/999/on')
        self.assertEqual(response.status_code, 500)  # Assuming 500 for invalid pin
        self.assertIn(b"Invalid pin number.", response.data)

    def test_invalid_action(self):
        """Test handling an invalid action."""
        response = self.app.get('/23/invalid')
        self.assertEqual(response.status_code, 500)  # Assuming 500 for invalid action
        self.assertIn(b"Invalid action", response.data)

    def test_pin_state_update(self):
        """Test if the pin state updates correctly after an action."""
        self.pins[23]['gpio'].read.return_value = 1
        response = self.app.get('/23/on')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.pins[23]['state'], 1)

if __name__ == "__main__":
    unittest.main()

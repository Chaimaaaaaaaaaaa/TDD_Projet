import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from servergpio import app, pins

class TestServerGPIO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.pins = pins

    @patch('servergpio.GPIO')
    def test_main_page_status(self, mock_gpio):
        """Test if the main page loads successfully."""
        mock_gpio.input.return_value = mock_gpio.LOW
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        for pin in self.pins:
            self.assertIn(f"GPIO {pin}".encode(), response.data)

    @patch('servergpio.GPIO')
    def test_turn_on_pin(self, mock_gpio):
        """Test turning a GPIO pin on."""
        response = self.app.get('/23/on')
        self.assertEqual(response.status_code, 200)
        mock_gpio.output.assert_called_with(23, mock_gpio.HIGH)
        self.assertIn(b"Turned GPIO 23 on.", response.data)

    @patch('servergpio.GPIO')
    def test_turn_off_pin(self, mock_gpio):
        """Test turning a GPIO pin off."""
        response = self.app.get('/23/off')
        self.assertEqual(response.status_code, 200)
        mock_gpio.output.assert_called_with(23, mock_gpio.LOW)
        self.assertIn(b"Turned GPIO 23 off.", response.data)

    @patch('servergpio.GPIO')
    def test_invalid_pin(self, mock_gpio):
        """Test handling an invalid pin."""
        response = self.app.get('/999/on')
        self.assertEqual(response.status_code, 500)  # Assuming 500 for invalid pin
        self.assertIn(b"Invalid pin number.", response.data)

    @patch('servergpio.GPIO')
    def test_invalid_action(self, mock_gpio):
        """Test handling an invalid action."""
        response = self.app.get('/23/invalid')
        self.assertEqual(response.status_code, 500)  # Assuming 500 for invalid action
        self.assertIn(b"Invalid action.", response.data)

if __name__ == "__main__":
    unittest.main()

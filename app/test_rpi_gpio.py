"""Tests d'integration de la classe RpiGpio avec la librairie RPi.GPIO"""

import RPi.GPIO as rpi  # pylint: disable=E0401
from rpi_gpio import RpiGpio

def test_rpi_gpio():
    """On teste l'ecriture et la lecture sur les pins GPIO 14 (output) et 
    GPIO 15 (input) de la Raspberry Pi.
    On relie les pins 14 et 15 avec un cable pour verifier avec les assert 
    que le code fonctionne correctement.
    """

    output_ = 14
    input_ = 15

    input_gpio = RpiGpio(input_)
    input_gpio.setmode("input")
    output_gpio = RpiGpio(output_)
    output_gpio.setmode("output")

    print("Test write 1 on the output pin")
    output_gpio.write(1)
    assert input_gpio.read() == rpi.HIGH

    print("Test write 0 on the output pin")
    output_gpio.write(0)
    assert input_gpio.read() == rpi.LOW

    print("end")


if __name__ == '__main__':
    test_rpi_gpio()

"""Module pour la gestion materielle des pins GPIO"""

import RPi.GPIO as rpi  # pylint: disable=E0401
from gpio import GPIO


class RpiGpio (GPIO):
    """Classe pour la gestion des pins GPIO sur Raspberry Pi"""

    def __init__(self, pin):
        """Constructeur de la classe RpiGpio"""
        super().__init__(pin)
        rpi.setmode(rpi.BCM)

    def setmode(self, mode):
        """Methode pour configurer le mode de la pin GPIO (INPUT/OUTPUT)"""
        if mode == "output":
            rpi.setup(self.num, rpi.OUT)
        elif mode == "input":
            rpi.setup(self.num, rpi.IN)
        else:
            raise ValueError("Invalid mode")
        super().setmode(mode)

    def getmode(self):
        """Methode pour recuperer le mode de la pin GPIO (INPUT/OUTPUT)"""
        return rpi.getmode()

    def write(self, value):
        """Methode pour ecrire une valeur sur la pin GPIO (LOW/HIGH)"""
        if self.getmode() == "output":
            raise ValueError("Pin is not configured as output.")

        rpi.output(self.num, rpi.HIGH if value else rpi.LOW)
        super().write(value)

    def read(self):
        """Methode pour lire la valeur de la pin GPIO (LOW/HIGH)"""
        if self.getmode() == "input":
            raise ValueError("Pin is not configured as input.")

        self.value = rpi.input(self.num)
        return super().read()

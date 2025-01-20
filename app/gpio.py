"""Module pour la gestion des pins GPIO"""

class GPIO :
    """Classe abstraite pour les pins GPIO"""

    def __init__(self, pin):
        """Constructeur de la classe GPIO"""
        self.num = pin
        self.mode = None
        self.value = None

    def setmode(self, mode):
        """Methode pour configurer le mode de la pin GPIO (INPUT/OUTPUT)"""
        if mode in ("output","input"):
            self.mode = mode
        else:
            raise ValueError("Invalid mode")

    def getmode(self):
        """Methode pour recuperer le mode de la pin GPIO (INPUT/OUTPUT)"""
        return self.mode

    def write(self, value):
        """Methode pour ecrire une valeur sur la pin GPIO (0/1)"""
        if self.mode == "input":
            raise ValueError("Pin is not configured as output.")
        self.value = value

    def read(self,):
        """Methode pour lire la valeur de la pin GPIO (0/1)"""
        if self.mode == "output":
            raise ValueError("Pin is not configured as input.")
        return self.value
    
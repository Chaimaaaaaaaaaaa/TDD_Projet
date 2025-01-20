from gpio import GPIO
import RPi.GPIO as rpi


class RPI_GPIO (GPIO):
    def __init__(self, pin):
        super().__init__(pin)
        rpi.setmode(rpi.BCM)
        
    def setmode(self, mode):
        if mode == "output":
            rpi.setup(self.num, rpi.OUT)
        elif mode == "input":
            rpi.setup(self.num, rpi.IN)
        else:
            raise ValueError("Invalid mode")
        super().setmode(mode)
    
    def getmode(self):
        return rpi.getmode()
        
    def write(self, value):
        if self.getmode() == "output":
            raise ValueError("Pin is not configured as output.")

        rpi.output(self.num, rpi.HIGH if value else rpi.LOW)
        super().write(value)
            
    def read(self):
        if self.getmode() == "input":
            raise ValueError("Pin is not configured as input.")
        
        self.value = rpi.input(self.num)
        return super().read()
    
    
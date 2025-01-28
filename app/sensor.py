import smbus2
from time import sleep

class MPL115A2:
    def __init__(self, bus=1, address=0x60):
        self.bus = smbus2.SMBus(bus)  
        self.address = address

    def read_coefficients(self):
        pass

    def read_raw_data(self):
        pass

    def get_pressure_temperature(self):
        pass

import smbus2
import time

class MPL115A2:
    def __init__(self, i2c_address=0x60, bus_num=1):
        self.address = i2c_address
        self.bus = smbus2.SMBus(bus_num)

    def start_conversion(self):
        pass

    def read_data(self):
        pass

    def write_register(self, register, value):
        pass
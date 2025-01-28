import smbus2
from time import sleep

class MPL115A2:
    def __init__(self, bus=1, address=0x60):
        self.bus = smbus2.SMBus(bus)  
        self.address = address
        #Coefficients de calibration stockés dans le capteur.
        self.a0 = None
        self.b1 = None
        self.b2 = None
        self.c12 = None
        self.read_coefficients()

    def read_coefficients(self):
        data = self.bus.read_i2c_block_data(self.address, 0x04, 8)
        #Les valeurs par lesquelles les données sont divisées dans ce code viennent de la documentation technique officielle du capteur MPL115A2. 
        self.a0 = (data[0] << 8 | data[1]) / 8.0
        self.b1 = (data[2] << 8 | data[3]) / 8192.0
        self.b2 = (data[4] << 8 | data[5]) / 16384.0
        self.c12 = ((data[6] << 8 | data[7]) >> 2) / 4194304.0

    def read_raw_data(self):
        self.bus.write_byte_data(self.address, 0x12, 0x00)
        sleep(0.003)

        data = self.bus.read_i2c_block_data(self.address, 0x00, 4)
        raw_pressure = (data[0] << 8 | data[1]) >> 6
        raw_temperature = (data[2] << 8 | data[3]) >> 6
        return raw_pressure, raw_temperature

    def get_pressure_temperature(self):
        pass

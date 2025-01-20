import smbus2
import time

class MPL115A2:
    def __init__(self, i2c_address=0x60, bus_num=1):
        self.address = i2c_address
        self.bus = smbus2.SMBus(bus_num)

    def start_conversion(self):
        self.bus.write_byte_data(self.address, 0x12, 0x00)
        time.sleep(0.003)

    def read_data(self):
        self.start_conversion()
        raw_pressure = self.bus.read_word_data(self.address, 0x00)
        raw_temperature = self.bus.read_word_data(self.address, 0x02)

        pressure = ((raw_pressure >> 8) & 0xFF) | ((raw_pressure & 0xFF) << 8)
        temperature = ((raw_temperature >> 8) & 0xFF) | ((raw_temperature & 0xFF) << 8)

        return {'pressure': pressure, 'temperature': temperature}

    def write_register(self, register, value):
        pass
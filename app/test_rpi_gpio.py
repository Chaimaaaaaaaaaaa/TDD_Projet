# test d'integration

from rpi_gpio import RPI_GPIO
import RPi.GPIO as rpi

def test_rpi_gpio():
    
    OUTPUT = 14
    INPUT = 15
    
    input_gpio = RPI_GPIO(INPUT)
    input_gpio.setmode("input")
    output_gpio = RPI_GPIO(OUTPUT)
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
    
    



from typing import Any


class GPIO :
    
    def __init__(self, pin):
        self.num = pin
        self.mode = None
        self.value = None
    
    def setmode(self, mode):
        pass
    
    def write(self, value):
        pass
    
    def read(self,):
        pass
    
    
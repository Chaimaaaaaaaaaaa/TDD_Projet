

class GPIO :
    
    def __init__(self, pin):
        self.num = pin
        self.mode = None
        self.value = None
    
    def setmode(self, mode):
        if mode == "output" or mode == "input":
            self.mode = mode
        else:
            raise ValueError("Invalid mode")
    
    def write(self, value):
        self.value = value 
    
    def read(self,):
        return self.value
    
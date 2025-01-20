

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
        
    def getmode(self):  
        return self.mode
    
    def write(self, value): 
        if self.mode == "input":
            raise ValueError("Pin is not configured as output.")
        else:
            self.value = value 
        
    
    def read(self,):
        if self.mode == "output":
            raise ValueError("Pin is not configured as input.")
        else:
            return self.value
    
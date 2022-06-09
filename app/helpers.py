def printMe(Message):
  print("Printing, ", Message)

class phones(): 
    def __init__(self,phoneOS,phoneVersion):
        self.os = phoneOS
        self.version =  phoneVersion

    def __str__(self):
        return self.os + ', ' + self.version

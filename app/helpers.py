
def printMe(Message):
  print("  #> Data: ", Message, "| Type: ", type(Message).__name__)
  
class phones(): 
    def __init__(self,phoneOS,phoneVersion):
        self.os = phoneOS
        self.version =  phoneVersion

    def __str__(self):
        return self.os + ', ' + self.version

class locations():
    def __init__(self,Lat,Long,City):
        self.latitude = Lat
        self.longitude =  Long
        self.City = City

    def __str__(self):
        return self.latitude + ', ' + self.longitude + ', ' + self.City
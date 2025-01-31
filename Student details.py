class CSStudent:
    stream = "cse"
    def _init_(self , roll):
        self.roll = roll
    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return self.address 
    
add = CSStudent(101)
add.setAddress = ("Pune, Maharashtra")
print(add.getAddress())

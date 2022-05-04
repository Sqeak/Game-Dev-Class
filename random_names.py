class Car:
    def __init__(self):
        
        self.make = "Kia"
        self.model = "Telluride"
        self.color = "Olive Green"
        self.year = "2021"
        
    def describe(self):
        print("I am a " + self.year,self.color,self.make,self.model)
        

myCar = Car()

myCar.describe()


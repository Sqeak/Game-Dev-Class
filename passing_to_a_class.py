class Car():
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = str(year)

    def describe(self):
        print("This is a", self.color, self.make, self.model, self.year)

newCar = Car("Kia", "Telluride", "Olive Green", "2022")

newCar.describe()
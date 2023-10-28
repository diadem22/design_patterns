import copy

class CarPrototype:
    def clone(self):
        return copy.copy(self)

class Car(CarPrototype):
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

original_car = Car("Toyota", "Camry", 2022, "Blue")
print("Original Car:", original_car)

copied_car = original_car.clone()
print("Copied Car:", copied_car)

copied_car.color = "Red"
print("Modified Copied Car:", copied_car)

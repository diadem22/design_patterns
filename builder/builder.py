class Car:
    def __init__(self, make, model, year, color, engine_type, doors, sunroof):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_type = engine_type
        self.doors = doors
        self.sunroof = sunroof

    def __str__(self):
        sunroof_str = "with Sunroof" if self.sunroof else "without Sunroof"
        return f"{self.year} {self.color} {self.make} {self.model}, {self.engine_type}, {self.doors} doors, {sunroof_str}"

class CarBuilder:
    def __init__(self, make, model, year):
        self.car = Car(make, model, year, None, None, None, None)

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine_type(self, engine_type):
        self.car.engine_type = engine_type
        return self

    def set_doors(self, doors):
        self.car.doors = doors
        return self

    def add_sunroof(self):
        self.car.sunroof = True
        return self

    def build(self):
        return self.car

car = CarBuilder("Toyota", "Camry", 2022) \
    .set_color("Blue") \
    .set_engine_type("V6") \
    .set_doors(4) \
    .add_sunroof() \
    .build()

print(car)

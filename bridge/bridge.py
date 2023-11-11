class Engine:
    def start(self):
        pass

class ElectricEngine(Engine):
    def start(self):
        print("Starting the car with an electric engine")

class GasolineEngine(Engine):
    def start(self):
        print("Starting the car with a gasoline engine")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        pass

class CarBrand(Car):
    def __init__(self, engine, brand):
        super().__init__(engine)
        self.brand = brand

    def start(self):
        print(f"Starting a {self.brand} car:")
        self.engine.start()


electric_engine = ElectricEngine()
gasoline_engine = GasolineEngine()

tesla = CarBrand(electric_engine, "Tesla")
bmw = CarBrand(gasoline_engine, "BMW")

tesla.start()
bmw.start()

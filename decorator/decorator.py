class Coffee:
    def cost(self):
        return 5 

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2  

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  

class FlavoringDecorator:
    def __init__(self, coffee, flavor):
        self._coffee = coffee
        self._flavor = flavor

    def cost(self):
        return self._coffee.cost() + 3  

    def description(self):
        return f"{self._flavor} {self._coffee.description() if hasattr(self._coffee, 'description') else 'coffee'}"


basic_coffee = Coffee()
print("Basic Coffee Cost:", basic_coffee.cost())


milk_coffee = MilkDecorator(basic_coffee)
print("Milk Coffee Cost:", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Sugar Milk Coffee Cost:", sugar_milk_coffee.cost())

vanilla_coffee = FlavoringDecorator(basic_coffee, "Vanilla")
print("Vanilla Coffee Cost:", vanilla_coffee.cost())
print("Vanilla Coffee Description:", vanilla_coffee.description())

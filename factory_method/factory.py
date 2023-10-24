class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"Product: {self.name}, Price: ${self.price}"


class ConcreteProductA(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = "Type A"


class ConcreteProductB(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = "Type B"


class ProductFactory:
    def create_product(self, name, price, product_type):
        if product_type == "A":
            return ConcreteProductA(name, price)
        elif product_type == "B":
            return ConcreteProductB(name, price)
        else:
            raise ValueError("Invalid product type")

\
factory = ProductFactory()

product1 = factory.create_product("Product 1", 10, "A")
product2 = factory.create_product("Product 2", 20, "B")

print(product1.describe())
print(product2.describe())

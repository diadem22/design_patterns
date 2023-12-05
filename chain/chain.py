from abc import ABC, abstractmethod

class OrderHandler(ABC):
    @abstractmethod
    def handle_order(self, order):
        pass

class KitchenHandler(OrderHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_order(self, order):
        if order == "Pizza":
            print("Kitchen: Pizza is being prepared.")
        elif self.next_handler:
            self.next_handler.handle_order(order)
        else:
            print("Kitchen: We cannot prepare this order.")

class BarHandler(OrderHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_order(self, order):
        if order == "Cocktail":
            print("Bar: Cocktail is being made.")
        elif self.next_handler:
            self.next_handler.handle_order(order)
        else:
            print("Bar: We cannot prepare this order.")

class Restaurant:
    def __init__(self):
        self.kitchen = KitchenHandler()
        self.bar = BarHandler()

        self.kitchen.next_handler = self.bar

    def place_order(self, order):
        self.kitchen.handle_order(order)

restaurant = Restaurant()

restaurant.place_order("Pizza")
restaurant.place_order("Cocktail")
restaurant.place_order("Burger")

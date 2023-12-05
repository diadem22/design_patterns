from abc import ABC, abstractmethod


class Chef:
    def prepare_pizza(self):
        print("Chef is preparing a pizza.")

    def prepare_pasta(self):
        print("Chef is preparing pasta.")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PizzaCommand(Command):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        self.chef.prepare_pizza()

class PastaCommand(Command):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        self.chef.prepare_pasta()


class Waiter:
    def __init__(self):
        self.orders = []

    def take_order(self, command):
        self.orders.append(command)

    def place_orders(self):
        for order in self.orders:
            order.execute()
        self.orders = [] 


chef = Chef()
pizza_command = PizzaCommand(chef)
pasta_command = PastaCommand(chef)

waiter = Waiter()
waiter.take_order(pizza_command)
waiter.take_order(pasta_command)

waiter.place_orders()

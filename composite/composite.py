from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def display_info(self):
        pass

class IndividualContributor(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"{self.position}: {self.name}")

class Manager(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        self.subordinates.remove(employee)

    def display_info(self):
        print(f"{self.position}: {self.name}")
        for subordinate in self.subordinates:
            subordinate.display_info()

individual1 = IndividualContributor("John", "Software Developer")
individual2 = IndividualContributor("Mark", "QA Engineer")

manager1 = Manager("Charlie", "Engineering Manager")
manager1.add_subordinate(individual1)
manager1.add_subordinate(individual2)

manager2 = Manager("David", "CTO")
manager2.add_subordinate(manager1)

print("Organizational Structure:")
manager2.display_info()

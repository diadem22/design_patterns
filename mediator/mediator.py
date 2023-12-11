class MessageMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} received: {message}")

mediator = MessageMediator()

user1 = User("Alice", mediator)
user2 = User("Bob", mediator)
user3 = User("Charlie", mediator)

mediator.add_user(user1)
mediator.add_user(user2)
mediator.add_user(user3)

user1.send("Hello, everyone!")

user2.send("Hey there!")

user3.send("Hi, folks!")

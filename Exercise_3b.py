import datetime

class Person:

    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

if __name__ == "__main__":
    Jane = Person()
    Bob = Person()
    Jane.add_pet("dog")

    print(Jane.pets)
    print(Bob.pets)


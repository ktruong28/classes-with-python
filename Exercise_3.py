import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname

if __name__ == "__main__":
    person = Person\
    (
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),
        "123 Sesame Street, Birdhouse Lane",
        "555 123 4567",
        "jane.doe@example.com"
    )

    print(person.name)
    print(person.email)
    print(person.age())
    print(person.age())

import datetime

class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname

if __name__ == "__main__":
    person = Person\
    (
        "Mrs",
        "Jane",
        "Doe"
    )

    print(person.title)
    print(person.name)
    print(person.surname)


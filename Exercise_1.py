import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

        self._age = None
        self._age_last_recalculated = None

        self._recalculate_age()

    def _recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= -1

        self._age = age
        self._age_last_recalculated = today

    def age(self):
        if datetime.date.today() > self._age_last_recalculated:
            self._recalculate_age()

        return self._age

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

"""
    We study class decorators - functions that are used to modify the behavior of other functions.
        @classmethod:
            (1) use constants or methods of a class w/o creating an instance of the class
            (2) used when inputs need formatting
        @staticmethod:
            (1) similar to classmethod but doesn't take any obligatory parameters (like a class/instance method)
"""

class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # instance method
    def fullname(self):
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith):
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith):
        return [t for t in Person.TITLES if t.endswith(endswith)]


Kevin = Person("Kevin", "Truong")

print(Kevin.fullname())

print(Kevin.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))

print(Kevin.allowed_titles_ending_with("r"))
print(Person.allowed_titles_ending_with("r"))
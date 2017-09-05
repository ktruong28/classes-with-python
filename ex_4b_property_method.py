"""
    We study class decorators - functions that are used to modify the behavior of other functions.
        @property:
            (1) use this decorator to make a method behave like a property i.e. no parentheses needed!
    There are decorators for which we can define a setter and a deleter for our attribute
"""

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)

    @fullname.setter
    def fullname(self, value):
        name, surname = value.split(" ", 1)
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname


kevin = Person("Kevin", "Truong")
print(kevin.fullname)

kevin.fullname = "Kelvin Tran"
print(kevin.fullname)
print(kevin.name)
print(kevin.surname)
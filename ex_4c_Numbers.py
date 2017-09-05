class Numbers(object):

    MULTIPLIER = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, xyval):
        self.x, self.y = xyval

    @value.deleter
    def value(self):
        del self.x
        del self.y


if __name__ == "__main__":
    num1 = Numbers(1, 2)
    print(num1.add())
    print(Numbers.multiply(3))
    print(Numbers.subtract(3, 1))
    print(num1.value)

    num1.value = (5, 6)
    print(num1.value)

    del(num1.value)
    print(hasattr(num1, "value"))

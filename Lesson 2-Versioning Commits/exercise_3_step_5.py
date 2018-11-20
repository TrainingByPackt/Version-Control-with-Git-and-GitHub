# Exercise 3: Adding Files to the Index

class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def add(self):
        pass

    def subtract(self):
        difference = 0
        for item in self.operands:
            difference -= item
        print(difference)

    def divide(self):
        pass

    def multiply(self):
        if self.operands is None:
            return
        product = 1
        for item in self.operands:
            product *= item
        print(product)

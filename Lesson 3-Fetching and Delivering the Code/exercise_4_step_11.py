# Exercise 4: Reversing Changes

class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def add(self):
        pass

    def subtract(self):
        pass

    def divide(self):
        quotient = 1
        for item in self.operands:
            quotient / item
        print(quotient)

    def multiply(self):
        pass

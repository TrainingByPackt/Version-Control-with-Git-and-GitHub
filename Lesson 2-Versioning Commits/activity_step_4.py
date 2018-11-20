class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def add(self):
        total = 0
        for item in self.operands:
           total += item
        print(total)

    def subtract(self):
        pass

    def divide(self):
        pass

    def multiply(self):
        pass

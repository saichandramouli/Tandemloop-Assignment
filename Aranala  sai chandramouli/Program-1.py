class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "Error: Cannot divide by zero."
        return self.a / self.b


# user inputs
a = input("Enter a: ")
b = input("Enter b: ")
op = input("Operation (add/sub/mul/div): ").lower()

calc = Calculator(a, b)

if op == "add":
    print("Result:", calc.add())
elif op == "sub":
    print("Result:", calc.sub())
elif op == "mul":
    print("Result:", calc.mul())
elif op == "div":
    print("Result:", calc.div())
else:
    print("Invalid operation")


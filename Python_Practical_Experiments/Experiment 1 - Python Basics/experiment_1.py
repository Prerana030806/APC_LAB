print("Python Basics")
name = input("Enter your name: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Hello,", name)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Division is not possible")
print("Data types:", type(name).__name__, type(a).__name__)

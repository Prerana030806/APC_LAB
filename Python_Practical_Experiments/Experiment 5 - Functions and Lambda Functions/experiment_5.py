def add(a, b):
    return a + b

def factorial(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

square = lambda number: number * number
maximum = lambda a, b: a if a > b else b

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print("Addition:", add(x, y))
print("Factorial of first number:", factorial(x))
print("Square of first number:", square(x))
print("Maximum:", maximum(x, y))

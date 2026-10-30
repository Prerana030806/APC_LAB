def is_happy(n):
    """
    Checks if a number is a happy number.
    Uses a set to detect cycles and prevent infinite loops.
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        sum_of_squares = 0
        for digit in str(n):
            sum_of_squares += int(digit) ** 2
        n = sum_of_squares
    return n == 1

print("Happy numbers from 1 to 100:")
happy_numbers = []
for i in range(1, 101):
    if is_happy(i):
        happy_numbers.append(i)

print(happy_numbers)
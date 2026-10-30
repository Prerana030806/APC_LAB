def find_pronic_numbers(limit):
    """
    Finds and prints all pronic numbers within a given limit.

    Args:
        limit (int): The upper bound (exclusive) for finding pronic numbers.
    """
    pronic_numbers = []
    n = 1
    while True:
        pronic = n * (n + 1)
        if pronic < limit:
            pronic_numbers.append(pronic)
            n += 1
        else:
            break
    print(f"Pronic numbers between 1 and {limit-1}:")
    print(*pronic_numbers)

# Call the function to find pronic numbers up to 100 (exclusive)
find_pronic_numbers(100)
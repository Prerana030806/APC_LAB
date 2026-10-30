def find_second_largest_sorted(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements to find a second largest

    # Remove duplicates and sort in ascending order
    unique_sorted_numbers = sorted(list(set(numbers)))

    if len(unique_sorted_numbers) < 2:
        return None # Not enough distinct elements

    return unique_sorted_numbers[-2]

# Example usage
my_list = [10, 5, 20, 15, 20, 8]
second_largest = find_second_largest_sorted(my_list)
print(f"The second largest number in {my_list} is: {second_largest}")
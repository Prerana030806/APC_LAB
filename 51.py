def find_smallest_with_min(numbers):
  """
  Finds the smallest number in a list using the built-in min() function.

  Args:
    numbers: A list of numbers.

  Returns:
    The smallest number in the list.
  """
  if not numbers:
    return None  # Handle empty list case
  return min(numbers)

# Example usage:
my_list = [5, 2, 8, 1, 7, 0, -3]
smallest_num = find_smallest_with_min(my_list)
print(f"The smallest number in the list {my_list} is: {smallest_num}")

empty_list = []
smallest_num_empty = find_smallest_with_min(empty_list)
print(f"The smallest number in the empty list is: {smallest_num_empty}")
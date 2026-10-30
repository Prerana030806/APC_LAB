def sum_list_builtin(numbers):
  """
  Calculates the sum of all items in a list using the built-in sum() function.

  Args:
    numbers: A list of numerical values.

  Returns:
    The sum of all items in the list.
  """
  return sum(numbers)

# Example usage
my_list = [1, 5, 8, 12, 3]
total_sum = sum_list_builtin(my_list)
print(f"The sum of items in the list {my_list} is: {total_sum}")
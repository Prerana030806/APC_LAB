def multiply_list_elements(numbers):
  """
  Multiplies all numbers in a given list and returns the product.

  Args:
    numbers: A list of numerical values (integers or floats).

  Returns:
    The product of all numbers in the list. Returns 1 if the list is empty.
  """
  product = 1
  for num in numbers:
    product *= num
  return product

# Example usage:
my_list1 = [1, 2, 3, 4, 5]
result1 = multiply_list_elements(my_list1)
print(f"The product of elements in {my_list1} is: {result1}")

my_list2 = [10, -2, 0.5]
result2 = multiply_list_elements(my_list2)
print(f"The product of elements in {my_list2} is: {result2}")

empty_list = []
result3 = multiply_list_elements(empty_list)
print(f"The product of elements in {empty_list} is: {result3}")
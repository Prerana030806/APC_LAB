def print_odd_numbers_in_list(numbers_list):
  print("Odd numbers in the list:")
  for number in numbers_list:
    if number % 2 != 0:  # Check if the number is odd (remainder when divided by 2 is not 0)
      print(number)

# Example usage:
my_list = [10, 15, 23, 42, 37, 51, 62, 5]
print_odd_numbers_in_list(my_list)

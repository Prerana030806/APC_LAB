def print_even_numbers(input_list):
  print("Even numbers in the list:")
  for number in input_list:
    if number % 2 == 0:
      print(number)

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(my_list)
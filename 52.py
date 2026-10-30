def find_largest_number(numbers):
  if not numbers:
    raise ValueError("The list cannot be empty.")
  
  largest = numbers[0]  # Initialize largest with the first element
  for number in numbers:
    if number > largest:
      largest = number
  return largest

# Example usage:
my_list = [10, 5, 20, 15, 8]
largest_number = find_largest_number(my_list)
print(f"The largest number in the list is: {largest_number}")
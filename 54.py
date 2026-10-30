def find_n_largest(input_list, n):
  if not input_list or n <= 0:
    return []

  # Sort the list in descending order
  input_list.sort(reverse=True)

  # Return the first N elements
  return input_list[:n]

# Example usage
my_list = [120, 50, 89, 170, 45, 250, 450, 340]
n_value = 4
largest_elements = find_n_largest(my_list, n_value)
print(f"The original list: {my_list}")
print(f"The {n_value} largest elements are: {largest_elements}")
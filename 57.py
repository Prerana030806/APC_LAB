def remove_empty_lists_comprehension(list_of_lists):
  return [sublist for sublist in list_of_lists if sublist]

# Example usage
my_list = [[1, 2], [], [3, 4], [], [5], []]
filtered_list = remove_empty_lists_comprehension(my_list)
print(f"Original list: {my_list}")
print(f"Filtered list (comprehension): {filtered_list}")
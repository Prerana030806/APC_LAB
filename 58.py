import copy
# Original list
original_list = [1, 2, [3, 4], 5]

# Method 1: Using slicing (shallow copy)
# This creates a new list, but for nested objects, it copies references.
sliced_copy = original_list[:]
print(f"Original list: {original_list}")
print(f"Sliced copy: {sliced_copy}")

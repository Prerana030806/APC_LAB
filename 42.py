dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1.copy()  # Create a copy to avoid modifying dict1 in-place
merged_dict.update(dict2)
print(merged_dict)
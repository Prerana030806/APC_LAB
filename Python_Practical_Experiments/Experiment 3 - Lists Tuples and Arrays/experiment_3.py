from array import array

numbers_list = [10, 20, 30, 40]
numbers_tuple = (5, 15, 25, 35)
numbers_array = array("i", [2, 4, 6, 8])

print("List:", numbers_list)
numbers_list.append(50)
numbers_list[0] = 100
print("Updated list:", numbers_list)
print("Tuple:", numbers_tuple)
print("Tuple element:", numbers_tuple[1])
print("Array:", numbers_array.tolist())
numbers_array.append(10)
print("Updated array:", numbers_array.tolist())
print("List length:", len(numbers_list))
print("Tuple length:", len(numbers_tuple))
print("Array length:", len(numbers_array))

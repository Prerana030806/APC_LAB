def is_harshad_number(number):
  """
  Checks if a given number is a Harshad (or Niven) number.

  Args:
    number: An integer.

  Returns:
    True if the number is a Harshad number, False otherwise.
  """
  if number <= 0:
    return False  # Harshad numbers are typically positive integers

  original_number = number
  sum_of_digits = 0

  # Calculate the sum of digits
  while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

  # Check if the original number is divisible by the sum of its digits
  return original_number % sum_of_digits == 0

# Example usage
num1 = 18
num2 = 156
num3 = 21

print(f"{num1} is a Harshad number: {is_harshad_number(num1)}")
print(f"{num2} is a Harshad number: {is_harshad_number(num2)}")
print(f"{num3} is a Harshad number: {is_harshad_number(num3)}")
print(f"0 is a Harshad number: {is_harshad_number(0)}")
print(f"-18 is a Harshad number: {is_harshad_number(-18)}")
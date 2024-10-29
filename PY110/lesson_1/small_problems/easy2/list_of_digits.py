# Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

# Input: integer
# Output: list of numbers
# requirements:
# integer will be positive
# convert integer to a list of integers

# Data structure: list

# algo:
# create a function that takes one argument: an integer
# convert that integer into a list of integers
# use the list function on the integer
# return result

# code


def digit_list(number):
    return [int(digit) for digit in str(number)]


print(digit_list(12345) == [1, 2, 3, 4, 5])  # True
print(digit_list(7) == [7])  # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])  # True
print(digit_list(444) == [4, 4, 4])  # True

# Write a function that takes one argument, a positive integer, and returns the sum of its digits.


def sum_digits(numbers):
    numbers_list = [int(num) for num in str(numbers)]

    return sum(numbers_list)


print(sum_digits(23) == 5)  # True
print(sum_digits(496) == 19)  # True
print(sum_digits(123456789) == 45)  # True
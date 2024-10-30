# Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.


def average(numbers_list):
    length = len(numbers_list)
    list_average = sum(numbers_list) // length
    return list_average


print(average([1, 5, 87, 45, 8, 8]) == 25)  # True
print(average([9, 47, 23, 95, 16, 52]) == 40)  # True
print(average([7]) == 7)  # True

# Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.


def invert_numbers(numbers):
    result = []

    for number in numbers:
        try:
            result.append(1 / number)
        except ZeroDivisionError:
            result.append(float("inf"))

    return result


numbers = [1, 2, 0, 3, 4]
print(invert_numbers(numbers))

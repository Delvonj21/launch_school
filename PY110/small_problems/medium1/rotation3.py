# Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.


def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)

    return number


def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)


def rotate_string(string):
    return string[1:] + string[0]


print(max_rotation(735291) == 321579)  # True
print(max_rotation(3) == 3)  # True
print(max_rotation(35) == 53)  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)  # True

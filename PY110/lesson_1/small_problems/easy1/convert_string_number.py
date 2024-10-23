# Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.


def string_to_integer(string):
    DIGITS = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    value = 0
    for char in string:
        value = (value * 10) + DIGITS[char]

    return value


def string_to_signed_integer(string):
    match string[0]:
        case "-":
            return -string_to_integer(string[1:])
        case "+":
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)  # True

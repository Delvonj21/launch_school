# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.


def stringy(num):
    result = ""

    for idx in range(num):
        if idx % 2 == 0:
            digit = "1"
        else:
            digit = "0"

        result += digit

    return result


print(stringy(6) == "101010")  # True
print(stringy(9) == "101010101")  # True
print(stringy(4) == "1010")  # True
print(stringy(7) == "1010101")  # True
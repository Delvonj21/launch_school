# Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.


def leading_substrings(string):
    result = []
    for idx in range(len(string)):
        sub_string = string[: idx + 1]
        result.append(sub_string)
    return result


# All of these examples should print True
print(leading_substrings("abc") == ["a", "ab", "abc"])
print(leading_substrings("a") == ["a"])
print(leading_substrings("xyzy") == ["x", "xy", "xyz", "xyzy"])

# Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.


def leading_substrings(string):
    result = []
    for idx in range(len(string)):
        sub_string = string[: idx + 1]
        result.append(sub_string)
    return result


# Initialize an empty list to store substrings.
# Iterate through the input string by index:
# For each index i from 0 to the last character of the string:
# Create a substring starting at the first character and ending at index i.
# Append the substring to the list.
# Return the list of substrings.


# All of these examples should print True
print(leading_substrings("abc") == ["a", "ab", "abc"])
print(leading_substrings("a") == ["a"])
print(leading_substrings("xyzy") == ["x", "xy", "xyz", "xyzy"])

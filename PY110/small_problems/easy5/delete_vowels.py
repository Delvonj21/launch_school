# Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.


def remove_vowel(string):
    VOWELS = "aeiouAEIOU"
    non_vowel = [char for char in string if char not in VOWELS]

    return "".join(non_vowel)


def remove_vowels(string_list):
    return [remove_vowel(string) for string in string_list]


# All of these examples should print True
original = ["abcdefghijklmnopqrstuvwxyz"]
expected = ["bcdfghjklmnpqrstvwxyz"]
print(remove_vowels(original) == expected)  # True

original = ["green", "YELLOW", "black", "white"]
expected = ["grn", "YLLW", "blck", "wht"]
print(remove_vowels(original) == expected)  # True

original = ["ABC", "AEIOU", "XYZ"]
expected = ["BC", "", "XYZ"]
print(remove_vowels(original) == expected)  # True

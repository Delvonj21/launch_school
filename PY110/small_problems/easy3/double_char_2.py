# Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

# You may assume that only ASCII characters will be included in the argument.

# Input: string
# Output: string
# rules:
# double every consonant in the string
# consonant is all letters excluding vowels  ('a','e','i','o','u')
# function should not double vowels, digits, punctuation, or whitespace

# data structure: string

# Algo
# create a function that takes a string as an argument
# create an empty string
# loop through each char in the string
# check weather char is a consonant
# if yes append that char to the new string, double
# if not just print that value alone


def is_consonant(char):
    vowels = "aeiouAEIOU"
    return char.isalpha() and char not in vowels


def double_consonants(string):
    doubled_string = ""

    for char in string:
        if is_consonant(char):
            doubled_string += char * 2
        else:
            doubled_string += char

    return doubled_string


# All of these examples should print True
print(double_consonants("String") == "SSttrrinngg")
print(double_consonants("Hello-World!") == "HHellllo-WWorrlldd!")
print(double_consonants("July 4th") == "JJullyy 4tthh")
print(double_consonants("") == "")

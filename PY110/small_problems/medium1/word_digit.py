# Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

# input: string
# output: a string with every occurrence of a "number word" converted to its corresponding digit
# rules:
# any word 1-9 will be converted to its digit
# rest of the string stays the same

# Data structure
# string, Dict

# Algo
# create a dictionary with the string_num as keys and digits as values
# check each word in the string against a key in the dictionary
# if the word appears as a key in the dictionary return its value
# return string with words converted to digits

NUMS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def word_to_digit(sentence):
    words = sentence.split()
    processed_words = [NUMS.get(word, word) for word in words]
    return " ".join(processed_words)


message = "Please call me at five five five one two three four"
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

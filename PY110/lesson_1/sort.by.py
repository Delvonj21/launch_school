# Input:
#     A list of strings
# Output:
#     a list of strings sorted according to the highest number
#   of adjacent consonants

# Explicit:
#     retain the original order if two strings contain the same highest number of adjacent consonants
# Adjacent consonants:
# - are next to each other in the same string
# - can have a space between them in adjacent words.


# Implicit:
# - Strings may contain single or multiple words.
# - Strings may not be empty.
# - Strings may have no adjacent consonants.
# - Strings should be sorted in descending order.
# - Case is not relevant.
# - Single consonants in a string do not affect sort order in
#   comparison to strings with no consonants. Only adjacent
#   consonants affect sort order.


# Question:
#     What is an adjacent consonant?
#     Do you need to handle cases where punctuation or special characters appear between consonants
# How should the function behave in the case of an empty string? Should it return an empty list or throw an error?
# How do you figure out the highest number of a character in a string?
# what about vowels and characters that aren't letters (numbers, punctuation)? How will you handle those? Should they be ignored, or do they break adjacency?

# Test cases
# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']

# Algorithm
# Identify which characters are consonants.
# Count how many adjacent consonants appear in each string.
# Sort the strings based on this count.

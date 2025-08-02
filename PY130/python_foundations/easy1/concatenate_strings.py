from functools import reduce

# Use reduce to concatenate a list of strings into a single string.

strings = ["The", " ", "Goat"]
concatenated = reduce(lambda x, y: x + y, strings)
print(concatenated)

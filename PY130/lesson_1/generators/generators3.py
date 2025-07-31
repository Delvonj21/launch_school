# Use a generator expression to capitalize every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.

strings = ["four", "score", "and", "seven", "years", "ago"]
capitalized = (string.capitalize() for string in strings)
print(tuple(capitalized))

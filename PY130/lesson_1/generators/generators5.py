# Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. Use a single print invocation to print all the capitalized strings as a set.

strings = ["four", "score", "and", "seven", "years", "ago"]

capitalized = (string.capitalize() for string in strings if len(string) >= 5)
print(set(capitalized))

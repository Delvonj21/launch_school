# Create a generator function that generates the capitalized version of every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.


def capitalized(strings):
    for string in strings:
        yield string.capitalize()


strings = ["four", "scores", "and", "seven", "years", "ago"]
print(tuple(capitalized(strings)))

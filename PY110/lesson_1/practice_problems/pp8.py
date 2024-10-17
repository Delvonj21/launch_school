# Given the following string, create a dictionary that represents the frequency with which each letter occurs. The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

char_freq = {}

statement = statement.replace(" ", "")
print(statement)
for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)

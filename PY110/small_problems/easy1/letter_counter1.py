# Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.


def word_sizes(string):
    words = string.split()
    word_counts = {}

    for word in words:
        length = len(word)
        word_counts.setdefault(length, 0)
        word_counts[length] += 1

    return word_counts


string = "Four score and seven."
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = "Hey diddle diddle, the cat and the fiddle!"
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = "Humpty Dumpty sat on a wall"
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes("") == {})

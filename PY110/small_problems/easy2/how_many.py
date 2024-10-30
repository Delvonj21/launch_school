# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").


def print_occurrences(word_counts):
    for key, value in word_counts.items():
        print(f"{key} => {value}")


def count_occurrences(items):
    word_counts = {}

    for word in items:
        word_counts.setdefault(word, 0)
        word_counts[word] += 1

    print_occurrences(word_counts)


vehicles = [
    "car",
    "car",
    "truck",
    "car",
    "SUV",
    "truck",
    "motorcycle",
    "motorcycle",
    "car",
    "truck",
]

print(count_occurrences(vehicles))

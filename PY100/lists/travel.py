destinations = [
    "Prague",
    "London",
    "Sydney",
    "Belfast",
    "Rome",
    "Aruba",
    "Paris",
    "Bora Bora",
    "Barcelona",
    "Rio de Janeiro",
    "Marrakesh",
    "New York City",
]

# Write a function that, without using the built-in in operator, checks whether a specific destination is included within destinations. For example: When checking whether 'Barcelona' is contained in destinations, the expected output is True, whereas the expected output for 'Nashville' is False.


def contains(element, lst):
    for item in lst:
        if element == item:
            return True

    return False


print(contains("Barcelona", destinations))  # True
print(contains("Nashville", destinations))  # False
print(contains("Chicago", destinations))  # False

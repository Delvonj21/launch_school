# Write a function that returns the last element of a list provided as an argument. For example:


def last(lst):
    if lst:
        return lst[-1]
    else:
        return None


print(last(["Earth", "Moon", "Mars"]))  # Mars

# Write a function that checks whether a string is empty or not. For example:


def is_empty(s):
    if not s:
        return True
    else:
        return False


print(is_empty("mars"))  # False
print(is_empty("  "))  # False
print(is_empty(""))  # True

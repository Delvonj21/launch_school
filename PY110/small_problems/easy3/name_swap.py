# Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.


def swap_name(string):
    first_name = string.split(" ")[0]
    last_name = string.split(" ")[1]

    return f"{last_name}, {first_name}"


print(swap_name("Joe Roberts") == "Roberts, Joe")  # True
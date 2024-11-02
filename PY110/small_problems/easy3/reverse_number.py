# Write a function that takes a positive integer as an argument and returns that number with its digits reversed.


def reverse_number(number):
    number_list = list(str(number))
    number_list.reverse()
    joined_int = int("".join(number_list))

    return joined_int


print(reverse_number(12345) == 54321)  # True
print(reverse_number(12213) == 31221)  # True
print(reverse_number(456) == 654)  # True
print(reverse_number(1) == 1)  # True
print(reverse_number(12000) == 21)  # True

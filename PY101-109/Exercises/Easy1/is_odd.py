# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.


def is_odd(number):
    if abs(number) % 2 != 0:
        return True
    else:
        return False


print(is_odd(3))
print(is_odd(2))

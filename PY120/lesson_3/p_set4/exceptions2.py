# Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.


# number = float(input("Enter a number: "))
# if number < 0:
#     raise ValueError("Negative numbers are not allowed")
# print(f"You entered {number}")

# Modify your answer from the previous problem to raise a custom exception named NegativeNumberError instead of an ordinary ValueError exception.


class NegativeNumberError(ValueError):
    pass


number = float(input("Enter a number: "))
if number < 0:
    raise NegativeNumberError("Negative numbers are not allowed!")
print(f"You entered {number}")

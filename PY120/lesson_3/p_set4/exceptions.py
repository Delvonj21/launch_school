# 1 Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential ZeroDivisionError or ValueError exceptions (there is no need to retry inputs in this problem).

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 / number2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("must enter a valid number!")

# 2 Expand your answer to the previous program so it prints the result only when no exceptions are raised. You should also print End of the program regardless of whether an exception is raised.

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 / number2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("must enter a valid number!")
else:
    print(f"The result is: {result}")
finally:
    print("End of the program")


# 3 Modify your answer to the previous problem so it handles both ZeroDivisionError and ValueError with a single exception handler. The output for both exception types can be obtained from the exception object.

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 / number2
except (ZeroDivisionError, ValueError) as e:
    print(e)
else:
    print(f"The result is: {result}")
finally:
    print("End of the program")

# What will the following code do and why? Don't run it until you have tried to answer.

a = 1


def my_function():
    a = 2


my_function()
print(a)

# The code will print the 1
# on Line 9 we use the global variable from Line 1 with the call to print, to print the value of the variable 'a' which is 1, the local variable has no effect on the global variable a

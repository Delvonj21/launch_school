# What will the following code do and why? Don't run it until you have tried to answer.

x = 10


def my_function():
    x = x + 5
    print(x)


my_function()

# The code will produce an UnboundLocalError
# In the function 'my_function', we attempt to reassign the value of 'x' by incrementing it, Python assumes the 'x' is a local variable since we're assigning it inside the function, but since it was never intialized we get an error, if you want to modify a variable in the global scope you must use the 'global' keyword

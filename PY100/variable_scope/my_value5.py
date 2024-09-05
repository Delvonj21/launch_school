# What will the following code do and why? Don't run it until you have tried to answer.

a = 1


def my_function():
    print(a)
    a = 2


my_function()

# The following code will have a UnboundLocalError

#  inside of the function Python detects that you are trying to assign the 'a' variable within the function so it treats it as a local variable
# but the assignment comes after the call to print causing an error

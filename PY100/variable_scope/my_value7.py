# What will the following code do and why? Don't run it until you have tried to answer.

a = 1


def my_function():
    global a
    a = 2


my_function()
print(a)

# the code will print 2
# On Line 7 we use the 'global' keyword, which tells the function that a refers to the global variable a. Any operation on the variable a inside of this function will affect the global variable a and not the local one.
# When we invoke the function on Line 11 the global variable is reassigned to the value of 2, then we print it

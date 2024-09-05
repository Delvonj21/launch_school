# What will the following code do and why? Don't run it until you have tried to answer.

a = 1


def my_function():
    print(a)


my_function()

# The code will print 1
# on Line 1 the variable 'a' is assigned to the value 1 in the global scope
# making it accessible inside the body of the function 'my_function'
# When we invoke the function 'my_function' on Line 8, it prints the value of the global variable a, which is 1

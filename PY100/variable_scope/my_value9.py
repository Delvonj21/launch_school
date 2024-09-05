# What will the following code do and why? Don't run it until you have tried to answer.

a = 7


def my_function(b):
    b += 10


my_function(a)
print(a)

# The code will print 7
# The function 'my_function' is invoked on Line 8 with the global variable of a and is used inside of the function, therefore changing the variable a to 17 but since integers are immutable, the local variable doesn't change the global variable on Line 3 so when we call to print we get the original global variable which is 7

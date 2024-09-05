# What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]


def my_function():
    b[0] = 10


my_function()
print(b)

# The code will print the list [10, 2, 3]
# on Line one we have a global variable with a list value [1, 2, 3], that list is then plugged into the function 'my_function'. The expression 'b[0] = 10 ' then mutates the list making it change into '[10, 2, 3]. Since list are mutable the global variable b is also changed

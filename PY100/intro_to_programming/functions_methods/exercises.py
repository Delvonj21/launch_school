# What happens when you run the following program? Why do we get that result?


def set_foo():
    foo = "bar"


set_foo()
print(foo)

# NameError: 'foo' is not defined, foo is a local variable that cannot be accessed outside of the function, therefore it is not in scope to execute the code

# What does this program print? Why?

foo = "bar"


def set_foo():
    foo = "qux"


set_foo()
print(foo)

# 'bar', 'bar' is a value that is assigned to the variable foo, which is defined in the global scope, which makes the variable accessible throughout the program
# The assignment on line 4 creates a new local variable that is local to the function


def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result


product = multiply_numbers(2, 3, 4)

# Identify the following items in that code:

# function name             # multiply_numbers()
# function arguments        # 2, 3, 4
# function definition       # multiply_numbers(num1, num2, num3):
#                                result = num1 * num2 * num3
#                                return result
# function body             # result = num1 * num2 * num3
# return result
# function parameters       # num1, num2, num3
# function invocation       # multiply_numbers(2, 3, 4)
# function return value     # 24
# all identifiers           # multiply_numbers, num1, num2, num3, result, product


# What does the following code print?


def scream(words):
    return words + "!!!!"


scream("Yipeee")  # doesn't print anything because there is no call to print

# What does the following code print?


def scream(words):
    words = words + "!!!!"
    return
    print(words)


scream(
    "Yipeee"
)  # doesn't print anything because the return statement terminates the function before the call to print

# Without running the following code, what do you think it will do?


def foo(bar, qux):
    print(bar)
    print(qux)


foo(
    "Hello"
)  # raise a TypeError, You need to provide 2 arguments because there are 2 parameters


# Without running the following code, what do you think it will do?


def foo(bar, qux):
    print(bar)
    print(qux)


foo(42, 3.141592, 2.718)
# raise a TypeError, there are more arguments then there are parameters


# Without running the following code, what do you think it will do?


def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo(42, 3.141592, 2.718)
# 42
# 3.141592
# 2.718
# the function foo is defined with 2 default parameters but 3 arguments were given, therefore Python ignores the default parameters and we use the 3 arguments given


# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# 42
# 3.141592
# 2
# the function foo is defined with 2 default parameters, and we get only two arguments here, so we have to use the default value for the last argument

# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# 42
# 3
# 2
# we have two default values for second and third here, since we only have one argument, Python uses the default values for the last two arguments

# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
# TypeError, no arguments were given and we only have default parameters for second and third identifiers. First parameter has no default value

# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# SyntaxError, Once Python sees a positional parameter with a default value, all subsequent parameters must have default values.

# Identify all of the identifiers on each line of the following code.

def multiply(left, right):              
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply Line 1, 9
# left Line 1, 2
# right Line 1, 2
# get_num Line 4, 7, 8
# first_number Line 7, 9, 10
# second_number Line 8, 9, 10
# product Line 9, 10
# prompt Line 4, 5
# float Line 5
# input Line 5
# print Line 10


# Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply global
# left  local
# right local
# get_num global
# prompt local
# first_number global
# second_number global
# product global
# float built-in
# input built-in
# print built-in


# In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function names:
# multiply: defined on line 1, used on line 9.
# get_num: defined on line 4, used on lines 7 and 8.
# float: built-in function used on line 5.
# input: built-in function used on line 5.
# print: built-in function used on line 10.
# Parameters:
# left and right are defined on line 1 and then used on line 2.
# prompt is defined on line 4 and then used on line 5.

# Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# Function names:
# say

# Method names:
# upper()
# lower()

# built-in functions:
# print
# input
# max

# The following function returns a list of the remainders of dividing the numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainders_3(numbers_1)))  # True
print(any(remainders_3(numbers_2)))  # True
print(any(remainders_3(numbers_3)))  # False
print(any(remainders_3(numbers_4)))  # False

# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_3(numbers_1)))   # False
print(all(remainders_3(numbers_2)))   # True
print(all(remainders_3(numbers_3)))   # False
print(all(remainders_3(numbers_4)))   # True
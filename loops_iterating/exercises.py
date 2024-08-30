# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# This code causes an infinite loop because there must be a way to increment the counter so that  `while counter < 5` eventually returns a falsy value

# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.

age = int(input("How old are you? "))
print(f"You are {age} years old.")
print()

for future in range(10, 50, 10):
    print(f"In {future} years, you will be {age + future} years old. ")


# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

while loop
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1

for loop

for nums in my_list:
    print(nums)


# Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])

    index += 1

for number in my_list:
    if number % 2 != 0:
        print(number)

# Print all of the even numbers in the following list of nested lists. Don't use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)


# you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

my_list = [
    1,
    3,
    6,
    11,
    4,
    2,
    4,
    9,
    17,
    16,
    0,
]

result = []
for number in my_list:
    if number % 2 == 0:
        result.append("even")
    else:
        result.append("odd")

print(result)

# Write a find_integers function that returns a list of all the integers from my_tuple:


def find_integers(things):
    return [element for element in things if type(element) is int]


my_tuple = (1, "a", "1", 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)  # [1, 3, -4]


# Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

my_set = {
    "Fluffy",
    "Butterscotch",
    "Pudding",
    "Cheddar",
    "Cocoa",
}

result = {name: len(name) for name in my_set if len(name) % 2 != 0}

print(result)


# Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result

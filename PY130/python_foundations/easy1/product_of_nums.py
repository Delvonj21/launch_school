from functools import reduce

# Calculate the product of all numbers in a list using the reduce function.


def multiply(x, y):
    return x * y


numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print(product)

# product = reduce(lambda x, y: x * y, numbers)
# print(product)

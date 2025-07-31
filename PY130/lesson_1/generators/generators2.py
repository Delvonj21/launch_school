# Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. Use a for loop to print each value.


def reciprocals(n):
    number = 1
    while number <= n:
        yield 1 / number
        number += 1


for value in reciprocals(7):
    print(value)

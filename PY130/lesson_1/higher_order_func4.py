# Use the reduce function shown in the answer to the previous question to compute the sum of the squares in a list of numbers.


def reduce(callback, iterable, start):
    accum = start

    for element in iterable:
        accum = callback(element, accum)

    return accum


numbers = [3, 7, 2, 9, 5]
squared = reduce(lambda number, accum: number**2 + accum, numbers, 0)
print(squared)

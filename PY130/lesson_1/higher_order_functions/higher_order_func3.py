def reduce(callback, iterable, start):
    accum = start
    for element in iterable:
        accum = callback(element, accum)

    return accum


numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))  # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))  # 300

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ""))  # ROYGBIV

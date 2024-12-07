# Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.


def is_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "scalene"


def is_valid(short, middle, long):
    return short > 0 and short + middle > long


def triangle(side1, side2, side3):
    total = side1 + side2 + side3
    short = min(side1, side2, side3)
    long = max(side1, side2, side3)
    middle = total - short - long

    if is_valid(short, middle, long):
        return is_triangle(side1, side2, side3)

    return "invalid"


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")  # True
print(triangle(0, 3, 3) == "invalid")  # True
print(triangle(3, 1, 1) == "invalid")  # True

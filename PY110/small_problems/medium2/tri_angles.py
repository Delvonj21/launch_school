# Write a function that takes the three angles of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

# You may assume that all angles have integer values, so you do not have to worry about floating point errors. You may also assume that the arguments are in degrees.


def is_right(angle):
    return angle == 90


def is_acute(angle):
    return angle < 90


def is_triangle(angles):
    if any([is_right(angle) for angle in angles]):
        return "right"
    elif all([is_acute(angle) for angle in angles]):
        return "acute"
    else:
        return "obtuse"


def is_valid(angles):
    total = sum(angles)
    non_zero = all([angle > 0 for angle in angles])
    return total == 180 and non_zero


def triangle(angles):
    angles = [angle1, angle2, angle3]

    if is_valid(angles):
        return is_triangle(angles)
    else:
        return "invalid"


print(triangle(60, 70, 50) == "acute")  # True
print(triangle(30, 90, 60) == "right")  # True
print(triangle(120, 50, 10) == "obtuse")  # True
print(triangle(0, 90, 90) == "invalid")  # True
print(triangle(50, 50, 50) == "invalid")  # True

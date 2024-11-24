# Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

# Note: You can use the following constant to represent the degree symbol:

DEGREE = "\u00b0"
MINUTES_PER_DEGREE = 60
SECONDS_PER_DEGREE = 60
SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_DEGREE


def pad_zeroes(number):
    number_string = str(number)
    if len(number_string) < 2:
        return "0" + number_string
    else:
        return number_string


def dms(degrees_float):
    degrees_int = int(degrees_float)
    minutes = int((degrees_float - degrees_int) * MINUTES_PER_DEGREE)
    seconds = int(
        (degrees_float - degrees_int - (minutes / MINUTES_PER_DEGREE))
        * SECONDS_PER_DEGREE
    )

    return f"{degrees_int}{DEGREE}" f"{pad_zeroes(minutes)}'" f'{pad_zeroes(seconds)}"'


print(dms(-1))  # -1°00'00"
print(dms(400))  # 400°00'00"
print(dms(-40))  # -40°00'00"
print(dms(-420))  # -420°00'00"

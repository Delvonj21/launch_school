# Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

# p
# write a function that takes a year and determines how many friday the 13ths are in that year

# e
# find all the friday the 13ths in the year given
# the year is greater than 1752, which is the modern Gregorian Calendar
# the same calendar will remain in use for the future

# d
# input: integer year
# output: integer
# data structure: integers

# a
# iterate over all the months of the given year
# for each month, get the day that falls on the 13th
# Count the 13ths that fall on a friday
# return count

import datetime


def friday_the_13ths(year):
    friday_13th = []

    for month in range(1, 13):
        date = datetime.date(year, month, 13)
        if date.weekday() == 4:
            friday_13th.append(date)

    return len(friday_13th)


print(friday_the_13ths(1986) == 1)  # True
print(friday_the_13ths(2015) == 3)  # True
print(friday_the_13ths(2017) == 2)  # True

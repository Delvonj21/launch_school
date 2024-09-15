# Build a program that displays when the user will retire and how many years she has to work till retirement.

import datetime

age = int(input("What is your age? "))
retire = int(input("At what age would you like to retire? "))

retired_age = retire - age

current_date = datetime.datetime.now()
year = current_date.year

print(f"It's {year}. You will retire in {year + retired_age}")
print(f"You have only {retired_age} years of work to go!")

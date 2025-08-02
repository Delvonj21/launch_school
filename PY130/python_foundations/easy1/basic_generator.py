# Create a generator function that yields numbers from 1 to 5.


def number_generator():
    for num in range(1, 6):
        yield num


for number in number_generator():
    print(number)

# Obtain only the even numbers from a list using the filter function.

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print(even_numbers)

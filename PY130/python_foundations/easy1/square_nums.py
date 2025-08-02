# Create a list where each number from the original list is squared using the map method.

numbers = [1, 2, 3, 4, 5]
transformed_numbers = list(map(lambda num: num**2, numbers))
print(transformed_numbers)

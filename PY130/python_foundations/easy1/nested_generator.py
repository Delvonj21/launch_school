# Use nested generator expressions to create a flat list of numbers from a list of lists.

nested_lists = [[1, 2, 3], [4, 5], [6, 7]]

flat_list = list((num for sublist in nested_lists for num in sublist))

print(flat_list)

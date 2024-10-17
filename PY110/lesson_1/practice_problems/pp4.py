# Given the following code, what would the output be? Try to answer without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# When we run this code we will get a dictionary with the names as keys  and index as values for each name in the `names` list

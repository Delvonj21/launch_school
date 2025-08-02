# Remove all None values from a list using the filter method.

values = ["The", None, None, "Dog", "Cat", None]
non_values = list(filter(lambda value: value is not None, values))
print(non_values)

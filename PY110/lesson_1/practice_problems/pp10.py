# What does the following code print and why?

dictionary = {"a": "ant", "b": "bear"}
print(dictionary.popitem())

# ('b', 'bear'), The `popitem()` method removes the last key / value pair in a dictionary and returns it as a tuple

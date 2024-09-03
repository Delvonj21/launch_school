# In your own words, explain the difference between these two expressions.

my_object1 == my_object2  # checks for equality, meaning if the two objects are equal, two collections are equal when they have the same elements
my_object1 is my_object2  # checks if they reference the same object, they are the same object if they are stored at the same location in memory

# Without running this code, what will it print? Why?

set1 = {42, "Monty Python", ("a", "b", "c")}
set2 = set1
set1.add(range(5, 10))
print(set2)

# {('a', 'b', 'c'), 'Monty Python', 42, range(5, 10)}
# if we add an element to set1, we'll see that element when we look at set2

# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    "Monty Python": "The Life of Brian",
    "Airplane!": "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2["Monty Python"] = "Holy Grail"
print(dict1["Monty Python"])

# 'The life of Brain'
#  dict2 is not the same object as dict1. When we change the value associated with the 'Monty Python' key in dict2, we don't see a corresponding change in dict1.

# Without running this code, what will it print? Why?
dict1 = {
    "a": [1, 2, 3],
    "b": (4, 5, 6),
}

dict2 = dict(dict1)
dict1["a"][1] = 42
print(dict2["a"])

# [1, 42, 3], dict
# dict(dict1) creates a new dict that contains the same key/value pairs as dict1. Thus, dict2 is not the same object as dict1.
# mutations to dict1['a'] can be seen in dict2['a'].


# Write some code to create a deep copy of the dict1 object and assign it to dict2. You should only modify the code where indicated.

# You may modify this line

dict1 = {
    "a": [[7, 1], ["aa", "aaa"]],
    "b": ([3, 2], ["bb", "bbb"]),
}

dict2 = dict1.copy.deepcopy(
    dict1
)  # deep copies create entirely new objects, including nested contents

# All of these should print False
print(dict1 is dict2)
print(dict1["a"] is dict2["a"])
print(dict1["a"][0] is dict2["a"][0])
print(dict1["a"][1] is dict2["a"][1])
print(dict1["b"] is dict2["b"])
print(dict1["b"][0] is dict2["b"][0])
print(dict1["b"][1] is dict2["b"][1])


# The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of dict1. Be careful: you're not allowed to use the copy module in this exercise.`

# In addition, before you run this code, can you predict the output values?

dict1 = {
    "a": [{7, 1}, ["aa", "aaa"]],
    "b": ({3, 2}, ["bb", "bbb"]),
}

dict2 = dict(dict1)  # dict() constructor creates a shallow copy of dict1

print(dict1 is dict2)
print(dict1["a"] is dict2["a"])
print(dict1["a"][0] is dict2["a"][0])
print(dict1["a"][1] is dict2["a"][1])
print(dict1["b"] is dict2["b"])
print(dict1["b"][0] is dict2["b"][0])
print(dict1["b"][1] is dict2["b"][1])

# The first print statement prints False since dict1 and dict2 are different objects.
# the nested components are all references to the original nested objects. Thus, the remaining print statements print True.

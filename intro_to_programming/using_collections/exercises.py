# Write Python code to print the seventh number of range(0, 25, 3).

my_range = range(0, 25, 3)
print(my_range[6])

# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

my_string = "Launch School"
print(my_string[4:10])

# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)

# This is a 3-part question. Consider the following dictionary:

pets = {
    "Cat": "Meow",
    "Dog": "Bark",
    "Bird": "Tweet",
}

# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
print(pets["Dog"])
# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
print(pets.get("Lizard"))
# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.
print(pets.get("Lizard", "<silence>"))

# Which of the following values can't be used as a key in a dict object, and why?

["a", "b"]  # all are mutable, keys in a dict must be hashable(immutable)
{"a": 1, "b": 2}
{1, 4, 9, 16, 25}

# What will the following code print?
print("abc-def".isalpha())  # False
print("abc_def".isalpha())  # False
print("abc def".isalpha())  # False
print("abc def".isalpha() and "abc def".isspace())  # False
print("abc def".isalpha() or "abc def".isspace())  # False
print("abcdef".isalpha())  # True
print("31415".isdigit())  # True
print("-31415".isdigit())  # False
print("31_415".isdigit())  # False
print("3.1415".isdigit())  # False
print("".isspace())  # False


# Write Python code to replace all the : characters in the string below with +.
info = "xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh"

print(info.replace(":", "+"))


# Explain why the code below prints different values on lines 3 and 4.
text = "It's probably pining for the fjords!"

print(text[21:35].rfind("f"))  # 8
print(text.rfind("f", 21, 35))  # 29

# On Line 2 The sequence is sliced first and the rfind searches the sliced sequence
# on Line 3 The sequence is searched first using rfind and then it is sliced

# Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ["hello", "world"],
    ["example", "mem", None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606


# Consider the following nested collection:

cats = {
    "Pete": {
        "Cheddar": {
            "color": "orange",
            "enjoys": {
                "sleeping",
                "snuggling",
                "meowing",
                "eating",
                "birdwatching",
            },
        },
        "Cocoa": {
            "color": "black",
            "enjoys": {
                "eating",
                "sleeping",
                "playing",
                "chewing",
            },
        },
    },
}

# Write one line of code to print the activities that Cocoa enjoys.
print(cats["Pete"]["Cocoa"]["enjoys"])

# Without running the following code, determine what each line should print.

print("johnson" in "Joe Johnson")  # False
print("sen" not in "Joe Johnson")  # True
print("Joe J" in "Joe Johnson")  # True
print(5 in range(5))  # False
print(5 in range(6))  # True
print(5 not in range(5, 10))  # False
print(0 in range(10, 0, -1))  # False
print(4 in {6, 5, 4, 3, 2, 1})  # True
print({1, 2, 3} in {1, 2, 3})  # False
print({3, 2} in {1, frozenset({2, 3})})  # True

# Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
print(3 in numbers1)  # True

numbers2 = []
print(3 in numbers2)  # False

numbers3 = [2, 4, 6, 8]
print(3 in numbers3)  # False

numbers4 = ["1", "3", "5"]
print(3 in numbers4)  # False

numbers5 = ["1", 3.0, "5"]
print(3 in numbers5)  # True

# Without running the following code, determine what each print statement should print.

cats = ("Cocoa", "Cheddar", "Pudding", "Butterscotch")

print("Butterscotch" in cats)  # True
print("Butter" in cats)  # False
print("Butter" in cats[3])  # True
print("cheddar" in cats)  # False

# Assume you have the following sequences:

my_str = "abc"
my_list = ["Alpha", "Bravo", "Charlie"]
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result so you can see all the values
print(zip(my_str, my_list, my_tuple, my_range))

# Without running the following code, what values will be printed by line 10?

pets = {
    "Cat": "Meow",
    "Dog": "Bark",
    "Bird": "Tweet",
}

keys = pets.keys()
del pets["Dog"]
pets["Snake"] = "Sssss"
print(keys)  # dict_keys(['Cat', 'Bird', 'Snake'])

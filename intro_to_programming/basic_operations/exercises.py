# Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value. For example, if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.

print("Delvon" + " Johnson")

# What does the following code do? Why?

print("5" + "10")  # '510'
# The code attempts to concatenate a string ('5') and an integer (10). In Python, you can't concatenate a string and an integer directly. The '+' operator is used for string concatenation, so this code will throw a TypeError.

# Refactor the code from the previous exercise to use coercion to print 15 instead.

print(int("5") + int("10"))  # 15

# Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:

foo = ["a", "b", "c"]
print(
    foo[3]
)  # will this result in an error? Yes, it will be an IndexError: list index out of range

# To what value does the following expression evaluate?

"foo" == "Foo"
# False, because in Python case matters. 'foo' and 'Foo' are different strings.

# What will the following code do? Why?

int("3.1415")  # ValueError
# It will raise a ValueError since the string 3.1415 does not represent a valid integer

# To what value does the following expression evaluate?
"12" < "9"
# True, Python performs a character-by-character comparison from left to right

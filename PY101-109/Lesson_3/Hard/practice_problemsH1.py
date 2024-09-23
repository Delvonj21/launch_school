# 1 Will the following functions return the same results?


def first():
    return {
        "prop1": "hi there",
    }


def second():
    return
    {
        "prop1": "hi there",
    }


print(first())
print(second())

# No, `first()` function will return the expected value `{"prop1": "hi there"}` but `second()` function will return `None`. In Python if nothing comes after the `return` statement it will return `None`

# 2 What does the last line in the following code output?

dictionary = {"first": [1]}
num_list = dictionary["first"]
num_list.append(2)

print(num_list)  # [1, 2]
print(dictionary)  # {'first': [1,2]}

# 3 Given the following similar sets of code, what will each code snippet print?

# A


def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one


one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# B


def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]


one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# C


def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"


one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

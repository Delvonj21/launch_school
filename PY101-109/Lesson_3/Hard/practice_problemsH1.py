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

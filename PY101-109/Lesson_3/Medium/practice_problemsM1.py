# 1 For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it.

for padding in range(1, 11):
    print(f'{"-" * padding}The Flintstones Rock!')

# 2 Alan wrote the following function, which was intended to return all of the factors of number:


def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result


# 3 Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer:


def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


# the first function mutates the original list. The second does not mutate the original list, but instead creates a new list and assigns it to 'buffer', whose value ultimately gets returned by the function

# 4 What will the following two lines of code output?

print(0.3 + 0.6)  # 0.8999999999999
print(0.3 + 0.6 == 0.9)  # False

# 5 What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))  # False

# 6 What is the output of the following code?

answer = 42


def mess_with_it(some_number):
    return some_number + 8


new_answer = mess_with_it(answer)

print(answer - 8)  # 34

# 7 One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}


def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"


mess_with_demographics(munsters)
# Yes, because dictionaries are mutable, when passed to a function, a reference to the dictionary is passed, not a copy. The changes made by Spot's 'demo_dict' directly affect the munsters dictionary.

# Function and method calls can take expressions as arguments. Suppose we define a function named rps as follows, which follows the classic rules of the rock-paper-scissors game, but with a slight twist: in the event of a tie, it just returns the choice made by both players.


def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"


# 8 What does the following code output?


print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))
# paper


# 9
def foo(param="no"):
    return "yes"


def bar(param="no"):
    return (param == "no") and (foo() or "no")


# What will the following function invocation return?

bar(foo())  # False

# 10 In Python, every object has a unique identifier that can be accessed using the id() function. This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning".

# Given the following code, predict the output:

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))  # True

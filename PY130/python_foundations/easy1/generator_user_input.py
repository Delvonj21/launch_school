# Create a generator function that yields user input strings until the word "stop" is entered.


def input_generator():
    while True:
        string = input("Enter a string: ")
        if string == "stop":
            break
        yield string


for user_input in input_generator():
    print(user_input)

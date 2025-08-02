# Use a generator expression to yield each character of a string in reverse order.

string = "Hello"

reverse_generator = (string[idx] for idx in range(len(string) - 1, -1, -1))

for char in reverse_generator:
    print(char)

# 1 If you have a list named people, how can you determine the number of entries in that list?

len(people)

# 2 Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ("hello", "world", "bye", "now")

# You will have to reassign the tuple, because tuples are immutable
# stuff = ('hello', 'world' 'goodbye', 'now')

# 3 Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.

# lists are mutable and tuples are immutable
# lists literals use [ ] and tuples literals use ( )

# lists and tuples are both sequences, meaning they are both ordered collections that can use numeric indexes to access the members
# lists and tuples are both heterogeneous, meaning that can use different types

# 4 Why can we treat strings as sequences?
# We can treat strings as sequences because strings are ordered and you can access the individual characters with indexing

# 5 How do the set types differ from the sequence types?
# Sets are unordered, they don't support indexing

# 6 Assuming you have the following assignment:
pi = 3.141592
# Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.

str_pi = str(pi)
print(str_pi)

# 7 Without running the following code, identify the numbers that are included in each of the following ranges:

range(7)  # [0, 1, 2, 3, 4, 5, 6]
range(1, 6)  # [1, 2, 3, 4, 5
range(3, 15, 4)  # [3, 7, 11]
range(3, 8, -1)  # [ ]
range(8, 3, -1)  # [8, 7, 6, 5, 4]


# 8 How would you print all the numbers in the following range?

print(list(range(3, 17, 4)))

# 9
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal? The two lists are equal: they are both lists with the same elements.
# Are the lists assigned to my_list and another_list the same object? The two lists are not the same object: The list constructor creates a new object.
# Are the nested lists at index 3 of my_list and another_list equal? The two nested lists are equal: they are both lists that have the same elements.
# Are the nested lists at index 3 of my_list and another_list the same object? The two nested lists are the same object: the list constructor creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied.

# 10 Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.
names = {"Chris", "Clare", "Karis", "Karl", "Max", "Nick", "Victor"}
print(names)
# It won't because its a set and sets are unordered

# 11 Consider the data in the following table:
# Name	Country
# Alice	USA
# Francois	Canada
# Inti	Peru
# Monika	Germany
# Sanyu	Uganda
# Yoshitaka	Japan

# You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

countries = {
    "Alice": "USA",
    "Francois": "Canada",
    "Inti": "Peru",
    "Monika": "Germany",
    "Sanyu": "Uganda",
    "Yoshitaka": "Japan",
}

print(countries["Monika"])

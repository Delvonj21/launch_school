# Using the class definition from problem 3, let's create some more people (Person objects):

# Without adding any code to the Person class, we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?


class Person:
    def __init__(self, name):
        self.name = name


bob = Person("Robert Smith")
rob = Person("Robert Smith")
print(bob.name == rob.name)

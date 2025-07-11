# Create a Person class with a "private" attribute _name. Use properties to create a getter and setter for the _name attribute. The _name attribute must be a string. Be sure to test your code.


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        self._name = name


person = Person("Delvon")
print(person.name)

person.name = "DJ"
print(person.name)

person.name = 1234
print(person.name)

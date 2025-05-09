# Create a Person class with two instance variables to hold a person's first and last names. The names should be passed to the constructor as arguments and stored separately. The first and last names are required and must consist entirely of alphabetic characters.

# The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), with both first and last names capitalized correctly.

# The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.

# Yes, this class is somewhat contrived.

# You can use the following code snippets to test your class. Since some tests cause exceptions, we've broken them into separate snippets.


class Person:
    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f"{first_name} {last_name}"

    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError("Name must be alphabetic.")

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name


actor = Person("Mark", "Sinclair")
print(actor.name)  # Mark Sinclair
actor.name = ("Vin", "Diesel")
print(actor.name)  # Vin Diesel
actor.name = ("", "Diesel")
# ValueError: Name must be alphabetic.

character = Person("annIE", "HAll")
print(character.name)  # Annie Hall
character = Person("Da5id", "Meier")
# ValueError: Name must be alphabetic.

friend = Person("Lynn", "Blake")
print(friend.name)  # Lynn Blake
friend.name = ("Lynn", "Blake-John")
# ValueError: Name must be alphabetic.

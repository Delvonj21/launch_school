# Create the methods needed so you can compare Cat objects for equality and inequality by their name value. The comparisons should ignore case and should work for the == and != operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.


class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() != other.name.casefold()


bugs = Cat("Bugs")
bugs2 = Cat("Bugs")
elmer = Cat("Elmer")

print(bugs == elmer)  # False
print(bugs == bugs2)  # True

print(bugs != elmer)  # True
print(bugs != bugs2)  # False

print(bugs == "Bugs")  # False
print(bugs != "Bugs")

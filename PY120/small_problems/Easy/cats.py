# Update this code so you see the following output when you run the code:


class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Cat(Pet):
    def __init__(self, name, age, colors):
        super().__init__(name, age)
        self._colors = colors

    @property
    def colors(self):
        return self._colors

    @property
    def info(self):
        return (
            f"My cat {self.name} is {self.age} " f"years old and has {self.colors} fur."
        )


cocoa = Cat("Cocoa", 3, "black")
cheddar = Cat("Cheddar", 4, "yellow and white")

print(cocoa.info)
print(cheddar.info)

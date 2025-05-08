#1 Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

class Player:
    def __init__(self, name):
        self.name = name

player1 = Player('Delvon')
player2 = Player('Kevin')


#2 Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.

class Foo:
    pass

foo = Foo()
print(f"I am a {type(foo).__name__} object")
print(f"I am a {foo.__class__.__name__} object")
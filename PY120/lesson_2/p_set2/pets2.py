# Create a new class called Cat, which can do everything a dog can, except fetch. Assume the methods do the exact same thing. Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.


class Pet:
    def speak(self):
        pass

    def sleep(self):
        return "sleeping!"

    def run(self):
        return "running!"

    def jump(self):
        return "jumping!"


class Dog(Pet):
    def speak(self):
        return "bark!"

    def fetch(self):
        return "fetching!"


class Bulldog(Dog):
    def sleep(self):
        return "snoring!"


class Cat(Pet):
    def speak(self):
        return "meow!"


pet = Pet()
brain = Dog()
bully = Bulldog()
kitty = Cat()

print(pet.run())
print(kitty.run())
print(kitty.speak())
try:
    kitty.fetch()
except Exception as exception:
    print(exception.__class__.__name__, exception, "\n")

print(brain.speak())

print(bully.run())
print(bully.sleep())

print([cls.__name__ for cls in Bulldog.mro()])
# ['Bulldog', 'Dog', 'Pet', 'object']

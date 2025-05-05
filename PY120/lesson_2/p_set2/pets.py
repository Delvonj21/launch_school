# Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"


class Dog:
    def speak(self):
        return "bark!"

    def sleep(self):
        return "sleeping!"


class Bulldog(Dog):
    def sleep(self):
        return "snoring!"


teddy = Dog()
dj = Bulldog()
print(teddy.speak())  # bark!
print(teddy.sleep())  # sleeping!
print(dj.speak())
print(dj.sleep())

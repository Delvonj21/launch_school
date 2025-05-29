# Define a Dog class that has a breed instance variable. Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. Print the breed of each dog.


class Dog:
    def __init__(self, breed):
        self._breed = breed

    # Add a get_breed method to the Dog class from your answer to the previous problem. The method should return the dog's breed. Use the method to print the breeds of the two dog objects you created in the previous problem. You should also mark the breed instance variable for internal use only.

    def get_breed(self):
        return self._breed


dog = Dog("Bulldog")
dog._breed = "Pitbull"
print(dog.get_breed())

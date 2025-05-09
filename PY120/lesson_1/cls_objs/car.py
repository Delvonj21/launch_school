# 1 Create a Car class that meets these requirements:

# Each Car object should have a model, model year, and color provided at instantiation time.

# You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.

# Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.

# Create a method that prints a message about the car's current speed.

# Write some code to test the methods.


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def engine_on(self):
        print("The engine is on!")

    def engine_off(self):
        self.speed = 0
        print("Lets slow down!")
        print("The engine is off!")

    def accelerate(self, number):
        self.speed += number
        print(f"You accelerated {number} mph!")

    def brake(self, number):
        self.speed -= number
        print(f"You decelerated {number} mph!")

    def check_speed(self):
        print(f"You are currently going {self.speed} mph!")


chevy = Car("chevy tahoe", 2002, "black")
chevy.engine_on()
chevy.accelerate(40)
chevy.check_speed()
chevy.brake(25)
chevy.check_speed()
chevy.brake(15)
chevy.check_speed()
chevy.engine_off()


# 2 Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests.


class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0

    # Omitted code

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year


# Omitted code
lumina = Car("lumina", 1997, "white")
print(f"My car is {lumina.color}.")
# My car is white.

print(f"My car's model is a {lumina.model}.")
# My car's model is a chevy lumina.

print(f"My car's year is {lumina.year}.")
# My car's year is 1997.

lumina.color = "brown"
print(f"My car is now {lumina.color}.")
# My car is now brown.

lumina.year = 2023
# AttributeError: property 'year' of 'Car' object
# has no setter


# 3 Add a method to the Car class that lets you spray paint the car a specific color. Don't use a setter method for this. Instead, create a method whose name accurately describes what it does. Don't forget to test your code.
class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color

    # Omitted code

    def spray_paint(self, color):
        self._color = color
        print(f"Your {color} paint job looks great!")


lumina.spray_paint("red")


# 4 Add a class method to your Car class that calculates and prints any car's average gas mileage (miles per gallon). You can compute the mileage by dividing the distance traveled (in miles) by the fuel burned (in gallons).


class Car:
    # Omitted code

    @classmethod
    def gas_mileage(cls, miles, gallons):
        mileage = miles / gallons
        print(f"{mileage} miles per gallon")


Car.gas_mileage(13, 351)

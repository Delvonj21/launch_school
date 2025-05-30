# Define a Student class that has a class variable named school_name. You should initialize the school name to 'Oxford'. After defining the class, instantiate an instance of the Student class and print the school name using that instance.


# class Student:
#     school_name = "Oxford"


# student = Student()
# print(student.__class__.school_name)


# Modify the Student class from your answer to the previous problem. The modified class should have an instance variable called name that gets initialized during instantiation. Create two Student objects with different names but the same school, then print the name and school for both students.


# class Student:
#     school_name = "Oxford"

#     def __init__(self, name):
#         self.name = name


# student1 = Student("Delvon")
# student2 = Student("Alice")

# print(student1.name, student1.__class__.school_name)
# print(student2.name, student2.__class__.school_name)

# Modify the Student class from your answer to the previous problem. The modified class should have a class method that returns the school's name. Without instantiating any Student objects, print the school's name in two different ways: once with the class method, and once by accessing the class variable directly.


class Student:
    school_name = "Oxford"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name


print(Student.get_school_name())
print(Student.school_name)

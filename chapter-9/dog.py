class Dog:
    """A simple attempt to model dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name 
        self.age = age

    def sit(self):
        """Simulating dog sitting in response of a command"""
        print(f"{self.name} is now sitting")  

    def roll_over(self):
        """Simulating dog rolling over in response of a command"""
        print(f"{self.name} rolled over")


my_dog = Dog("Willie", 6)
your_dog = Dog('Lucy', 1)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's  is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog's  is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()
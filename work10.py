class Dog:
    def __init__(self, name):
        self.name = name  # Use self.name, not self.Name with a capital 'N'

dog1 = Dog("Buddy")  # Create an instance of the Dog class
print(dog1.name)  # Access and print the 'name' attribute of the dog1 instance
"""Create a Person class with properties like name and age.
Instantiate objects and display the details using class methods."""

class Person:

    # Class Variable
    company = "NTEK employee:"
    position = "Web developer"
    language = "Python programmer"

    # The init method or constructor
    def __init__(self, name, age):

        # Instance Variable
        self.name = name
        self.age = age

# Objects of person class
Info = Person("Jason Iverson", "23")

print('Exercise 1')
print('Personal Information:')
print('My name is', Info.name)
print("I am " + Info.age + " years old\n")

# Access using class
print(Person.company)
print(Person.position)
print(Person.language)
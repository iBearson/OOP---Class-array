""" Implement a Student class with private properties.
Create methods to set and get student grades, ensuring validation."""

class Student:
    # Encapsulated Properties
    def __init__(self, name):
        self.__name = name      
        self.__grade = None      

    # Method to set grade with validation
    def set_grade(self, grade):
        if 0 <= grade <= 100:   
            self.__grade = grade
        else:
            print("Error: Grade must be between 0 and 100.")

    def get_grade(self):
        return self.__grade

    def get_name(self):
        return self.__name

# Student Objects
student1 = Student("Jason")
student2 = Student("LeBron")

# Setting 
student1.set_grade(85)
print(f"{student1.get_name()}'s grade: {student1.get_grade()}")

# Attempting to set an invalid grade for validation
print(f"{student2.get_name()}'s grade: {student2.get_grade()}")
student2.set_grade(105)  
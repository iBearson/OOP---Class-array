""" Create a Vehicle class and derive Car and Bike classes. """

# Base class 
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"This is my favorite {self.brand} {self.model}."

# Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def info(self):
        return f"{self.describe()} With a color of {self.color}."

# Bike class that inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        return f"{self.describe()} It's a {self.bike_type} bike."

# Create objects
favorite_car = Car("Toyota", "Trueno AE86", "Black and White")
favorite_bike = Bike("Vespa", "Sprint", "Scooter")

# Display info
print("Exercise 2")
print(favorite_car.info())     
print(favorite_bike.info())   


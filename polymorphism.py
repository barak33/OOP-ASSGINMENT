# Base class
class Entity:
    def __init__(self, speed, color):
        self.speed = speed  # Speed in appropriate units (e.g., km/h)
        self.color = color  # Color of the entity

    def move(self):
        pass  # Abstract method, to be overridden in subclasses

    def show_details(self):
        return f"Speed: {self.speed} km/h, Color: {self.color}"

# Animal class
class Animal(Entity):
    def move(self):
        print(f"Running 🐾 at {self.speed} km/h!")

# Bird class
class Bird(Entity):
    def move(self):
        print(f"Flying ✈️ through the skies at {self.speed} km/h!")

# Fish class
class Fish(Entity):
    def move(self):
        print(f"Swimming 🐟 at {self.speed} km/h in {self.color} waters!")

# Car class
class Car(Entity):
    def move(self):
        print(f"Driving 🚗 down the road at {self.speed} km/h!")

# Plane class
class Plane(Entity):
    def move(self):
        print(f"Flying ✈️ across the clouds at {self.speed} km/h!")

# Train class
class Train(Entity):
    def move(self):
        print(f"Riding on rails 🚂 at {self.speed} km/h!")

# Example usage
entities = [
    Animal(15, "brown"),
    Bird(60, "blue"),
    Fish(5, "silver"),
    Car(120, "red"),
    Plane(900, "white"),
    Train(180, "green")
]

for entity in entities:
    entity.move()
    print(entity.show_details())

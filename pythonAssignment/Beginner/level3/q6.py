"""6. Create the custom Python classes which have methods and attributes and implement single inheritance,
        multiple inheritance, and multilevel inheritance
"""

# Base class
class Vehicle:
    def start(self):
        return "Vehicle started"

# Single inheritance
class Car(Vehicle):
    def drive(self):
        return "Car is driving"

# Multiple inheritance
class Electric:
    def charge(self):
        return "Charging electric battery"

class Gasoline:
    def refuel(self):
        return "Refueling gasoline tank"

# Multiple inheritance combining Electric and Gasoline
class HybridCar(Electric, Gasoline):
    def mode(self):
        return "Hybrid mode activated"

# Multilevel inheritance extending Car
class SportsCar(Car):
    def turbo(self):
        return "Turbo mode activated"

class RaceCar(SportsCar):
    def race(self):
        return "Racing at high speed!"


print("----- Vehicle -----")
v = Vehicle()
print(v.start())

print("\n----- Car -----")
c = Car()
print(c.start())   # inherited from Vehicle
print(c.drive())

print("\n----- HybridCar -----")
h = HybridCar()
print(h.charge())  # from Electric
print(h.refuel())  # from Gasoline
print(h.mode())

print("\n----- RaceCar -----")
r = RaceCar()
print(r.start())   # from Vehicle via Car
print(r.drive())   # from Car
print(r.turbo())   # from SportsCar
print(r.race())    # from RaceCar

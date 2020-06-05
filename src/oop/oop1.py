# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Establish a Parent class, this being Vehicle, the other classes are children.

# Base/Parent class
class Vehicle:
    pass

# Child of Vehicle/Parent of Car/Motorcycle
class GroundVehicle(Vehicle):
    pass

# Child of GroundVehicle
class Car(GroundVehicle):
    pass

# Child of GroundVehicle
class Motorcycle(GroundVehicle):
    pass

#Child of Vehicle/Parent of Airplane/Starship
class FlightVehicle(Vehicle):
    pass

# Child of FlightVehicle
class Airplane(FlightVehicle):
    pass

# Child of FlightVehicle
class Starship(FlightVehicle):
    pass
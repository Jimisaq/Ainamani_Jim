#Abstraction
#A class that contains one or more methods
#Abstract class and interfaces

from abc import ABC, abstractmethod
#Starting a car engine and bike
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #method has no implementation

#Child class implementing the abstract method
class Car(Vehicle):
    def start(self):
        print("Car engine started")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

#Notes:
#We cannot create an object of an abstract class
# vehicle1 = Vehicle() would raise an error
car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()

#Exercise
#Submit your work on GitHub for Method overriding, method overloading and MRO

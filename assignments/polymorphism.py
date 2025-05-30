#Polymorphism
from tokenize import String

from multipledispatch import dispatch

@dispatch(str)
def introduce_self(name):
    print("My name is " + name)

@dispatch(str,int)
def introduce_self(name,age):
    print("My name is " + name+". I am " + str(age) + " years old.")

introduce_self("Jim")
introduce_self("Isaac",20)
print('\n\n')

#Overring

class Animal:

    def sound(self):
        print('Animal making sound')

class Dog(Animal):
    def sound(self):
        print('Dog barking...')

class Cat(Animal):
    def sound(self):
        print('Cat meowing...')

#The overridden methods in subclasses are called
animal1 = Dog()
animal1.sound()

animal2 = Cat()
animal2.sound()

#Method Resolution Order
#Mostly relevant when there is multiple inheritance
class Vehicle(Animal):
    def fuel(self):
        print('Adding fuel...')

class Car(Vehicle):
    def fuel(self):
        print('Adding more fuel.')

class Motorcycle(Vehicle):
    def fuel(self):
        print('Adding less fuel.')

class TukuTuku(Car, Motorcycle):
    pass

vehicle = TukuTuku()
vehicle.fuel()

#Outputs the order of method resolution for objects of the TukuTuku class
print(TukuTuku.mro())

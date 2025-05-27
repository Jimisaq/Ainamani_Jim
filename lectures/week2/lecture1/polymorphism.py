#Example three: Polymorphism with inheritance
#Superclass
class Bird:
    def fly(self):
        print("Bird flies in the sky")

#derived class
class Eagle(Bird):
    def fly(self):
        print("Eagle flies at high altitudes")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies at low altitudes")

#How we use polymorphism
def test_flight(bird):
    bird.fly() #Run respective fly method based on the object type

#Creating objects
eagle1 = Eagle()
sparrow1 = Sparrow()
#Testing polymorphism
test_flight(eagle1)
test_flight(sparrow1)

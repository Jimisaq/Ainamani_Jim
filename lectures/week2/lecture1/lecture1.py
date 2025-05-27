#object oriented programming
class LivingThing:
    def breathe(self):
        print("Living thing breathes")
class Animal:
    def speak(self):
        print("Animal makes sound")

class Cat(Animal, LivingThing):
    def sound(self):
        print("Cat makes sound Meow")

cat1= Cat()
cat1.speak()  # Inherited method from Animal class
cat1.sound()
cat1.breathe()# Method from Cat class
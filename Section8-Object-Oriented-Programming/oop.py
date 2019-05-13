## INHERITANCE
# Parent class

class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myAnimal = Animal()

# Child class
class Dog(Animal):
    def _init_(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def speak(self):
        return self.name + " says woof!"

myDog = Dog()
print(myDog.speak())

# Child class
class Cat(Animal):
    def _init_(self):
        Animal.__init__(self)
        print("Cat Created")

    def speak(self):
        return self.name + " says meow!"
myCat = Cat()
print(myCat.speak())

## POLYMORPHISM
boston = Dog("Boston")
kitty = Cat("Kitty")

# Function that takes both classes
for pet in [boston, kitty]
    print(type(pet))
    print(pet.speak())


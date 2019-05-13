## INHERITANCE

# Parent class
class Animal:
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


myAnimal = Animal()

# Child class
class Lion(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Lion Created")


myLion = Lion()
myLion.who_am_i

## POLYMORPHISM
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat:
    def __init__(self, name):
        self.name = name
        print("Cat Created")

    def speak(self):
        return self.name + " says meow!"


boston = Dog("Boston")
kitty = Cat("Kitty")

# Function that takes both classes
for pet in [boston, kitty]:
    print(type(pet))
    print(pet.speak())


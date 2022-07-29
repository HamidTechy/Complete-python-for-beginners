class Animal:
    def walk(self):
        print("walk")


class Dog(Animal): # this is inheritence which means child get something from their parents
    def bark(self):
        print("My dog barking")


class Cat(Animal):
    pass   # python don't like empty class therefor pass mean nothing


tommy = Dog()
tommy.bark()
mano = Cat()
mano.walk()
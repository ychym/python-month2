class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def make_sound(self):
        print(f"Animals make a different sound")

    # @property
    # def age(self):
    #     return self.__age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

class Dog(Animal):
    def make_sound(self):
        print(f"{self.get_name()} is barking")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.get_name()} is miaowing")

dog1 = Dog("Akdosh", 2)
cat1 = Cat("Saryk", 4)

print(f"The dog's name is {dog1.get_name()}.Now his age is {dog1.get_age()} and next year will be {dog1.set_age(3)}.")
print(f"The cat's name is {cat1.get_name()}.Her age is {cat1.get_age()}.")

animals = [dog1, cat1]
for a in animals:
    a.make_sound()

#parent or base class or super class
# class Car:
#     def __init__(self,color,horse_power):
#         self.color=color
#         self.horse_power=horse_power
#
#     def driving_to(self,destination):
#         print(f"Car {self.color} is driving to {destination}")
#
#     def change_color(self,new_color):
#         self.color=new_color
#         print(f"Car color changed to {new_color}")

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        # Реализация абстрактного метода
        print("Собака лает")

class Cat(Animal):
    def make_sound(self):
        # Реализация абстрактного метода
        print("Кошка мяукает")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()
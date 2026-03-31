"""Polymorphism (Көп түрдүүлүк)"""
#parent or base class or super class
class Car:
    def __init__(self,color,horse_power):
        self.color=color
        self.horse_power=horse_power

    def driving_to(self,destination):
        print(f"Car {self.color} is driving to {destination}")

    def change_color(self,new_color):
        self.color=new_color
        print(f"Car color changed to {new_color}")
#child or derived class

class Bus(Car):
    def __init__(self,color,horse_power,number_seats):
        super().__init__(color,horse_power)#parent class ka kairyluu.When method __init__, super() required!
        self.number_seats=number_seats

    def driving_to(self, destination):
        print(f"Bus {self.color} is driving to {destination}")

class Truck(Car):
    def change_color(self,new_color):
        self.color=new_color
        print(f"Truck color changed to {new_color}")
car_1=Car("purple",500)
bus_1=Bus("blue",200,20)
truck_1=Truck("white",300)
#Polymorphism (Көп түрдүүлүк)↓
vehicles=[car_1,bus_1,truck_1]
for v in vehicles:
    v.driving_to(destination="Osh")



"""Inheritance-Murastoo"""
# #parent or base class or super class
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
# #child or derived class
#
# class Bus(Car):
#     def __init__(self,color,horse_power,number_seats):
#         super().__init__(color,horse_power)#parent class ka kairyluu.When method __init__, super() required!
#         self.number_seats=number_seats
#
#     def driving_to(self, destination):
#         print(f"Bus {self.color} is driving to {destination}")
#
# class Truck(Car):
#     def change_color(self,new_color):
#         self.color=new_color
#         print(f"Truck color changed to {new_color}")
#
# bus_1=Bus("blue","200",20)
# bus_1.driving_to("Bishkek")
# print(bus_1.color)
# print(type(bus_1))
# print(f"The type of bus1  is a bus:",isinstance(bus_1,Bus))
# print(f"The type of bus1  is a car:",isinstance(bus_1,Car))#parent class bolgon uchun result is True
#
# truck_1=Truck("white",300)
# print(truck_1.change_color("red"))
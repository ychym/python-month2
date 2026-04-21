class Animal:
    def move(self):
        print("Animal is moving")

#swimming and flying ??
class Swimming(Animal):
    def move(self):
        super().move()
        print("Swimming")

class Flying(Animal):
    def move(self):
        super().move()
        print("Flying")

class Duck(Flying, Swimming):
    def move(self):
        super().move()
        print("Duck is swimming and flying")


duck1 = Duck()
duck1.move()
# method resolution order чечүү тартиби
print(Duck.__mro__)
# Do poniższej klasy dopisz metodę statyczną która wypisze liczbę obiektów (piesków)
# znajdujących się w liście i wypisze imiona wszystkich obiektów.
# Przetestuj kod na co najmniej dwóch obiektach.

class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def wyswietl():
        print("liczba obiektow: ", Dog.count)
        print("imiona:", ', '.join(Dog.dogs))


d1 = Dog('koks')
d2 = Dog('laz')
d3 = Dog('kaz')

Dog.wyswietl()

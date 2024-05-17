# Napisz prostą klasę Student która będzie posiadać atrybuty takie jak imię i numer albumu.
# Utwórz 3 różne obiekty tej klasy.

class Student:
    def __init__(self, imie, nr_albumu):
        self.imie = imie
        self.nr_albumu = nr_albumu

    def print(self):
        print(self.imie, " ", self.nr_albumu)


s1 = Student('karol', 111111)
s2 = Student('bartek', 222222)
s3 = Student('kacper', 333333)

s1.print()
s2.print()
s3.print()
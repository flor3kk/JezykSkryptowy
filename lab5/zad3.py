# Napisz klasę Osoba która będzie posiadać atrybuty takie jak imię i nazwisko.
# Edytuj klasę Student by dziedziczyła po klasie osoba i dodatkowo posiadała atrybut numer_albumu.
# Utwórz 3 różne obiekty tej klasy a następnie wypisz informacje o nich.

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Osoba):
    def __init__(self, imie, nazwisko, nr_albumu):
        super().__init__(imie, nazwisko)
        self.nr_albumu = nr_albumu

    def print(self):
        print(self.imie, " ", self.nazwisko, " ", self.nr_albumu)


s1 = Student('karol', 'krawczyk', 111111)
s2 = Student('bartek', 'ja', 222222)
s3 = Student('kacper', 'luza', 333333)

s1.print()
s2.print()
s3.print()

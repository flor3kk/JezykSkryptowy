# Do klasy Student dopisz metodę po której wywołaniu student się przedstawi.
# Cześć nazywam się imię nazwisko i mój numer albumu to nr_albumu

class Student:
    def __init__(self, imie, nr_albumu):
        self.imie = imie
        self.nr_albumu = nr_albumu

    def print(self):
        print("czesc nazywam sie: ", self.imie, " i moj numer albumu to: ", self.nr_albumu)


s1 = Student('karol', 111111)

s1.print()

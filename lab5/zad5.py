# Napisz klasę Liczba mającą jeden atrybut przechowujący liczbę i nadpisz
# wybraną z magicznych metod tak aby realizowała działanie x^2+2xy+y

# class Liczba:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Liczba x={self.x}, y={self.y}"
#
#     def __licz__(self):
#         return self.x ** 2 + (2 * self.x * self.y) + self.y
#
#
# l1 = Liczba(1, 1)
#
# print(l1.__repr__())
# print("wynik: ", l1.__licz__())

class Liczba:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"Liczba x={self.x}, y={self.y}"

    def __add__(self, other):
        return self.x ** 2 + (2 * self.x * other) + other


l1 = Liczba(1)
l2 = Liczba(1)

wynik = l1+l2
print(wynik)


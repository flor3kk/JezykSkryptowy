# zadanie 5
def licz(x):
    return x ** 2 + 5 * x - 4


def decor(func):
    def a(x):
        wzor = func.__name__
        print(f"rownanie: {wzor}")
        print("============")
        print(f"wynik: {func(x)}")
        print("============")
    return a


funk_dekorujaca = decor(licz)
funk_dekorujaca(5)
import datetime

# ZAD2
# imie = input("podaj imie: ")
# print(f"siema: {imie}")

# ZAD3
# zakres = int(input("podaj zakres: "))
# suma = 0
# for _ in range (0, zakres):
#     liczba = int(input())
#     suma += liczba
# print(f"oto twoja suma: {float(suma)}")

# SKROCONA WERSJA
# print(sum(int(x) for x in input("liczby ").split()))

# ZAD4
# print(sum(int(x) for x in range(8, 81))) moje
# print(sum(range(8, 81))) szefa

# ZAD5
# x = datetime.date.today()
# print(x)

# rok = int(input("podaj rok"))
# miesiac = int(input("podaj miesiac"))
# dzien = int(input("podaj dzien"))
# date = datetime.date(rok, miesiac, dzien)

# print(x - date)

# ZAD6
def add(arg1, arg2):
    print(arg1 + arg2)

def div(arg1, arg2):
    if arg2 == 0:
        print("Blad")
    else:
        print(arg1 / arg2)

def mul(arg1, arg2):
    print(arg1 * arg2)

def min(arg1, arg2):
    print(arg1 - arg2)

def start():
    x = int(input("podaj liczbe a: "))
    y = int(input("podaj liczbe b: "))

    while True:
        choice = int(input("podaj dzialanie: 1-dodawanie, 2-dzielenie, 3-mnozenie, 4-odejmowanie 5-wyjscie "))
        if choice == 1:
            add(x, y)
        elif choice == 2:
            div(x, y)
        elif choice == 3:
            mul(x, y)
        elif choice == 4:
            min(x, y)
        else:
            print("koniec")
            break

start()
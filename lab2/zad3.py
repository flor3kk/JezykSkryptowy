import math

def add(arg1, arg2):
    print(f"WYNIK DODAWANIA {arg1} + {arg2}")
    print(arg1 + arg2)


def div(arg1, arg2):
    print(f"WYNIK DZIELENIA {arg1} / {arg2}")
    if arg2 == 0:
        print("Blad")
    else:
        print(arg1 / arg2)


def mul(arg1, arg2):
    print(f"WYNIK MNOZENIA {arg1} * {arg2}")
    print(arg1 * arg2)


def min(arg1, arg2):
    print(f"WYNIK ODEJMOWANIA {arg1} - {arg2}")
    print(arg1 - arg2)


def pole(arg1):
    metoda = f"obliczania pola dla promienia {arg1}"
    print(f"POLE KOLA O PROMIENIU {arg1}")
    wynik = round(math.pi * (arg1 ** 2))
    print(wynik)
    save(metoda, wynik)


def obwod(arg1):
    metoda = f"obliczania obwodu dla promienia {arg1}"
    print(f"OBWOD KOLA O PROMIENIU: {arg1}")
    wynik = round(2 * math.pi * arg1)
    print(wynik)
    save(metoda, wynik)

def save(metoda, wynik):
    file = open("pliczek.txt", "a")
    file.write(f"wynik dzialania {metoda}: "+str(wynik)+ "\n")
    file.close()

def start():
    x = int(input("podaj liczbe a: "))
    y = int(input("podaj liczbe b: "))

    while True:
        choice = int(input("podaj dzialanie: \n1-dodawanie, \n2-dzielenie,\n"
                           "3-mnozenie,\n4-odejmowanie\n"
                           "5-pole kola(tylko pierwsza liczba bedzie brana pod uwage\n"
                           "6-obwod kola(tylko pierwsza liczb bedzie brana pod uwage\n"
                           "7- wyjscie "))
        if choice == 1:
            add(x, y)
        elif choice == 2:
            div(x, y)
        elif choice == 3:
            mul(x, y)
        elif choice == 4:
            min(x, y)
        elif choice == 5:
            pole(x,)
        elif choice == 6:
            obwod(x)
        else:
            print("koniec")
            break

start()

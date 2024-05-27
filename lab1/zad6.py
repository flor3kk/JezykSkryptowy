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

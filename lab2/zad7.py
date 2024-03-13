import math


def obliczanie(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b * -math.sqrt(delta)) / (2 * a)
        x1 = round(x1, 3)
        x2 = (-b * + math.sqrt(delta)) / (2 * a)
        x2 = round(x2, 3)
        print(f"oto rozwiazania: x1 = {x1}, x2 = {x2}")
        info = f"delta wieksza od 0: {delta}: jej wyniki to: x1 = {x1}, x2 = {x2}"
        save(info)

    elif delta == 0:
        x0 = -b / 2 * a
        print(f"oto jedno rozwiazanie: x0 = {x0}")
        info = f"delta rowna {delta}, jej wynik to x0 = {x0}"
        save(info)
    else:
        info = f"delta mniejsza od 0: {delta}, wiec brak rozwiazan"
        print(f"delta mniejsza od 0: {delta} wiec nie ma rozwiazan")
        save(info)


def save(info):
    with open("rownania.txt", "a") as file:
        file.write(f"{info}\n")


obliczanie(int(input("podaj pararmetr a:")),
           int(input("podaj pararmetr b:")),
           int(input("podaj pararmetr c:")))

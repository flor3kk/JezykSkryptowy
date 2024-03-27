#ZADANIE 3
import random

tab = []

def save(info):
    with open("pliczek.txt", "a") as file:
        file.write(f"tablica: {info}\n")

wielkosc = int(input("podaj wielkosc tablicy: "))
for i in range(0, wielkosc):
    tab.append(random.randint(-5, 5))

save(tab)

print("Wysiwietlanie tablicy")
for i in tab:
    print(i, " | ", end='')
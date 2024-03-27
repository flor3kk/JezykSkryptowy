#ZADANIE 2
tab = []

while True:
    znak = input("podaj znak: (quit aby wyjsc)")
    if znak.lower() == "quit":
        break
    tab.append(znak.lower())


for i in reversed(tab):
    print(i + " | ", end='')

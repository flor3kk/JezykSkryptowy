import random


def lotto():
    lista = []
    while len(lista) < 6:
        los_liczba = random.randint(1, 49)
        if  los_liczba not in lista:
            lista.append(los_liczba)

    return lista

print(lotto())
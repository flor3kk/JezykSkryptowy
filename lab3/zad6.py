# ZADANIE 6
import random


def deck():
    figura = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    kolor = ['♣', '♦', '♥', '♠']
    return [(fig, kol) for fig in figura for kol in kolor]


def shuffle_deck(list):
    random.shuffle(list)
    return list


def deal(talia, n):
    if len(talia) < 5 * n:
        print("brak kart")

    rozdane = []
    for i in range(n):
        reka = []
        for j in range(5):
            reka.append(talia.pop())
        rozdane.append(reka)
    return rozdane


if __name__ == '__main__':
    talia = deck()
    print("OTO TALIA", talia)

    print("POSORTOWANA TALIA: ", shuffle_deck(talia))

    rece = deal(talia, 4)
    for i, reka in enumerate(rece, start=1):
        print(f"reka gracza: {i}")
        for karta in reka:
            print(f"{karta[0]} {karta[1]}")
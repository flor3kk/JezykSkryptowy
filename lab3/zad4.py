#ZADANIE 4
import numpy

def matrix():
    tab = numpy.zeros((5, 5), dtype=int)
    tab[0] = numpy.arange(2, 7)

    for i in range(1, 5):
        tab[i] = tab[i - 1] ** 2

    return tab

tablica = matrix()
print(tablica)
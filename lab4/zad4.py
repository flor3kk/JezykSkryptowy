# zadanie 4
def generuj(slowko):
    for i in range(1, len(slowko) + 1):
        yield slowko[:i]


slowo = 'pozdrawiam'
lista_liter = list(generuj(slowo))
print(lista_liter)
def licz(lista):
    return sum(lista)

def odczytaj_z_pliku(nazwa_pliku, funkcja_sumowania):
    with open(nazwa_pliku, 'r') as plik:
        liczby = [int(line.strip()) for line in plik]
    suma = funkcja_sumowania(liczby)
    print("Suma liczb z pliku:", suma)

# Przykładowe użycie:
plik = "liczby.txt"  # Załóżmy, że plik zawiera liczby, każda w nowej linii
odczytaj_z_pliku(plik, licz)

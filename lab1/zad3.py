zakres = int(input("podaj zakres: "))
suma = 0
for _ in range(0, zakres):
    liczba = int(input())
    suma += liczba
print(f"oto twoja suma: {float(suma)}")

# SKROCONA WERSJA
# print(sum(int(x) for x in input("liczby ").split()))

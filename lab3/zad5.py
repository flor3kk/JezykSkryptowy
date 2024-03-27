#ZADANIE 5
def ilosc(path):
    histogram = {}

    with open(path, 'r') as plik:
        tekst = plik.read()

        for znak in tekst:
            if  znak in histogram:
                histogram[znak] += 1
            else:
                histogram[znak] = 1

    return histogram

test = ilosc("pliczek.txt")
print("dokument: ", test)
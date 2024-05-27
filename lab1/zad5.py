import datetime

x = datetime.date.today()
print(x)

rok = int(input("podaj rok"))
miesiac = int(input("podaj miesiac"))
dzien = int(input("podaj dzien"))
date = datetime.date(rok, miesiac, dzien)

print(x - date)

#Zadania
# 1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 elementy
krotka = (1,2,3)
lista = [4,5,6]
slownik = {"A" : 1,
           "B" : 8,
           "C" : 9}
zbior = {10,11,12}


# 2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów
print(f"Dlugosc krotki: {len(krotka)}")
print(f"Dlugosc listy: {len(lista)}")
print(f"Dlugosc slownika: {len(slownik)}")
print(f"Dlugosc zbioru: {len(zbior)}")


# 3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów
print("Elementy krotki:")
for i in krotka:
    print(i)

print("Elementy lista:")
for i in lista:
    print(i)

print("Elementy slownik:")
for i in slownik.items():
    print(i)

print("Elementy zbior:")
for i in zbior:
    print(i)


# 4. Teraz wypisz wartości słownika zamiast kluczy
print("Wartosći słownika:")
for value in slownik.values():
    print(value)

# 5. Wypisz te same elementy w odwrotnej kolejności, 
# czy zawsze jest to możliwe bezpośrednio?
# * podpowiedzi:
# - [start:stop:step] np. [::1] - wypisze wszystkie elementy
# - tylko struktury z indeksami można iterowac od końca (konwersja)

print("Krotka odwrotnie:")
for i in krotka[::-1]:
    print(i)


print("Lista odwrotnie:")
for i in lista[::-1]:
    print(i)


print("Zbiór odwrotnie:")
for i in list(zbior)[::-1]:
    print(i)


# 6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.

# 7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.

# 8. Sprawdź długość listy.

# 9.Zamień listę na krotkę- krotka2 i sprawdź jej długość.

# 10.Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, z czego wynika różnica?
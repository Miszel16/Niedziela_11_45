# Czym jest lista? (3 znane metody)

# STRUKTURY DANYCH

print(f'Krotki:')
# 1. KROTKI (TUPLES) ------------------------------------------
# - „rekord”, który jest stały
# - dane logicznie tworzą jedną całość i nie chcesz ich zmieniać
# - np. punktu (x, y), daty (rok, miesiac, dzien), wyniku funkcji (kilka wartości na raz)
# - Można używać jako kluczy w słowniku (bo jest niemodyfikowalna)

#         x, y
punktA = (2,12)
dataA = (2026,1,18)

krotka = (4,) # krotka

zmienna = (4) # zmienna typu int

# MOTODY
# 1. Zliczanie elementow opodanej wartości [.count()]
krotka_test = (2,2,2,2,5,6,7)

ile_2 = krotka_test.count(2)
print(f"Ile '2' w krotce: {ile_2}")

# 2. Znalezienie pierwszego indeksu o danej wartości [.index()]
indeks = krotka_test.index(6) # 5
print(f"Pod którym indeksem '6': {indeks}")





print(f'\n\n\nZbiory:')
# 2. ZBIORY (SETS) -----------------------------------------------
# - unikalne elementy + matematyka na zbiorach
# - usuwa duplikaty !!!!!!
# - operacje typu: część wspólna, różnica, suma zbiorów
# - nie może zawierać listy

zbior = {1,2,3,4,4,4,4}
print(zbior) # 1,2,3,4

zbior_pusty = set()
print(zbior_pusty)

# METODY
# 1. Dodanie elementu do zbioru [.add()]
zbior.add(7)
zbior.add(1)
zbior.add(0)
print(zbior)

# 2. Usunięcie elementu o podaje wartości [.remove()]
zbior.remove(4)
print(f"Po usunięciu '4': {zbior}")


# 3. Usunięcie elementu jeżeli istnieje [.discard()]
zbior.discard(7)
print(f"Po usunięciu '7': {zbior}")


# 4. Usunięcie pierwszego elementu i zwrócenie go [.pop()]
element = zbior.pop()
print(f"Co usuwamy: {element}\nZbiór po usunięciu:{zbior}")


# 5. Czyszczenie zbioru [.clear()]
zbior.clear()
print(zbior) # set()



# ------------------- ZESTAWIENIE WSZYTSKICH DOTYCHCZASOWYCH STRUKTUR -------------------
print(f"\n\n\nKonwersje:\n")
# KONWERSJE MIĘDZY STRUKTURAMI

zbior = {1,2,3}   # set()
krotka = (4,5,6)  # tuple()
lista = [7,8,8,9] # list()

print("Zbior na liste:")
print(f"{list(zbior)}   {type(list(zbior))}\n")

print("Krotka na liste:")
print(f"{list(krotka)}   {type(list(krotka))}\n")


print("Zbiór na krotke:")
print(f"{tuple(zbior)}   {type(tuple(zbior))}\n")

print("Lista na krotke:")
print(f"{tuple(lista)}   {type(tuple(lista))}\n")


print("Krotka na zbiór:")
print(f"{set(krotka)}   {type(set(krotka))}\n")

print("Lista na zbiór:")
print(f"{set(lista)}   {type(set(lista))}\n")
# * Co było ostatnio?
# - słownik w pythonie
# - JSON to format globalny


# Rozgrzewka
# Napisz listę zawierająca 10 różnych wartości, a następnie wypisz co drugą:

lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,len(lista),2):
    # print(lista[i])
    pass


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# 1. Co znamy do tej pory?
# - przechowywanie danych (różne typy danych),
# - indeksy (od przodu (0) | od tyłu (-1)),
# - możliwa modyfikacja (.append(), .pop())





# 2. METODY
#--------------------------------------------------------------------------------
# 1) utworzenie listy
moja_lista = [23, "Tekst", 1.333, True, 16, "kot"]
print(f"Moja lista:\n{moja_lista}")


#--------------------------------------------------------------------------------
# 2) dodawanie elementów na koniec listy [.append()]
moja_lista.append("Pies")
print(f"Moja lista:\n{moja_lista}")


#--------------------------------------------------------------------------------
# 3) !! poszerzenie listy o element po którym można iterować [.extend()]
imiona = ["Aleksander", "Ola", "Jan", "Adam", "Maurycy", "Olek", "Patryk", "Fabian"]
moja_lista.extend(imiona)
print(f"Moja lista:\n{moja_lista}\n")


#--------------------------------------------------------------------------------
# 4) !! dodawanie pod wskazany indeks [.insert()]
print(f"{list(enumerate(moja_lista))}\n")

moja_lista.insert(11, "Pinokio")

print(f"{list(enumerate(moja_lista))}\n")

#--------------------------------------------------------------------------------
# 5) !! usuwanie elementu o konkretnej wartości [.remove()]
# * usuwa pierwszy pasujący
# * co jeśli nie znajdzie?
moja_lista.append("kot")

print(f"Moja lista:\n{moja_lista}")
moja_lista.remove("kot")
print(f"Moja lista:\n{moja_lista}")


#--------------------------------------------------------------------------------
# 6) !! usunięcie elementu spod wskazanego indeksu i ZWRÓCENIE GO [.pop()]
# * co jeśli nie znajdzie?
print(f"{list(enumerate(moja_lista))}\n")

# lista = [1,  2,  3]
# #        0   1   2
# #       -3  -2  -1

element = moja_lista.pop(1)

print(f"Usunięty element: {element}")
print(f"Moja lista:\n{moja_lista}")


#--------------------------------------------------------------------------------
# 7) !! znajdowanie indeksu dla podanej wartości [.index()]
# * zwraca pierwszy pasujący
# * co jeśli nie znajdzie?

moja_lista.append("kot")

print(f"{list(enumerate(moja_lista))}\n")

# I - pierwszy znaleziony
id = moja_lista.index("kot")
print(f"{id}\n")


# II - szukanie od indeksu (włącznie)
id = moja_lista.index("Pies",4)
print(f"{id}\n")


# III - szukanie w przedziale
# start, stop, (step) 
id = moja_lista.index("Pies", 0,5)
print(f"{id}\n")


#--------------------------------------------------------------------------------
# 8) zliczanie wsytąpień danej wartości [.count()]

ile = moja_lista.count("kot")
print(f"Koty:{ile}")



#--------------------------------------------------------------------------------
# 9) !! sortowanie listy [.sort()]
# * elementy muszą dać się ze sobą porównać (str != int -> nie zadziała)
print("Nowa lista:")
lista = [5,7,3,2,22,6,1]
print(lista)
lista.sort()
print(lista)



#--------------------------------------------------------------------------------
# 10) !! odwrócenie kolejności listy [.reverse()]
print("Lista reverse:")
print(lista)
lista.reverse()
print(lista)


#--------------------------------------------------------------------------------
# 11) !! kopiowanie listy [.copy()]
kopia_lista = lista.copy()
print(f"Lista oryginalna: {lista}")
print(f"Lista kopia: {kopia_lista}")



#--------------------------------------------------------------------------------
# 12) czyszczenie listy [.clear()]
print(moja_lista)
moja_lista.clear()
print(moja_lista)


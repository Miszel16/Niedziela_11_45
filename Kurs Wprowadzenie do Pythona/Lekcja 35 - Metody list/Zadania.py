# Zadania 

# 1 Stwórz 2 listy składające się z 3 liczb każda
lista1 = [1,2,3]
lista2 = [4,5,6]


# 2 Połącz stworzone wcześniej listy
lista1.extend(lista2)
print(lista1)


# 3 Usuń elementy z indeksami 2 i 5 , który element należy usunąć najpierw?
# lista1.pop(5)
# lista1.pop(2)
# print(lista1)


# 4 Usuń największą i najmniejszą liczbę z listy (zakładamy że nie znamy)
lista1.remove(min(lista1))
lista1.remove(max(lista1))
print(lista1)


# 5 Dodaj liczbę do listy
lista1.append(0)
print(lista1)

# 6 Posortuj listę
lista1.sort()
print(lista1)


# 7 Utwórz kopię listy
kopia_lista = lista1.copy()
print(f"lista oryginalna: {lista1}")
print(f"lista kopia: {kopia_lista}")


# 8 Odwróć kolejność elementów w kopii
# 9 Dodaj do każdej wartości w pierwszej listy 1, a w drugiej odejmij 1
# 10 Wyświetl obie listy
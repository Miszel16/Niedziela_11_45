# Algorytm 

# Lista wygenerowania do testowania
# - 20 losowych elementów (1-100)
import random

lista_test = []

for i in range(20):
    wartosc = random.randint(1,100)
    lista_test.append(wartosc)

#print(lista_test)

# ------------------------------------------------------------------------
# Słownik - krótko

osoba = {
    "imie": "Alicja",
    "nazwisko": "XYZ",
    "wiek": 20,
    "adres": {
        "ulica": "Kwiatowa",
        "numer": 10,
        "miasto": "Kraków"
    }
}

# słownik: osoba, 4 klucze:
#   - imie (str)
#   - nazwisko (str)
#   - wiek (int)
#   - adres [słownik zagnieżdżony (3 klucze):
#                - ulica (str)
#                - numer (int)
#                - miasto (str)
#                ]
# print(osoba)

print(f"{osoba}\n")

# # ----------------- OPERACJE NA SŁOWNIKACH -----------------
# - dodanie nowej pary klucz - wartość:
osoba["wzrost"] = 175.00
osoba["hobby"] = "programowanie"

print(f"{osoba}\n")


# - usunięcie pary klucz-wartość:
del osoba["wiek"]
print(f"{osoba}\n")


# - dostęp do wartości na podstawie klucza:
print(osoba["imie"])


# - iteracja przez pary klucz-wartość w słowniku:
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc},")

print("\n\n\n\n\n")
# ------------------------------------------------------------------------
# 1. SORTOWANIE BĄBELKOWE (bubble sort) O(n*n)
# wizualizacja:
# https://commons.wikimedia.org/wiki/File:Bubble-sort.gif
# https://www.sortvisualizer.com/bubblesort/

# 0 1 2  - len= 3

def bubble_sort(lista: list):
    n = len(lista)
    # przejść po wszytskich elementach - iterowanie
    for i in range(n):
        for j in range(0, n-1-i):
            # porównaj sąsiadów
            if lista[j] > lista[j+1]:
                # zamień miejscami
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(lista_test)
print(bubble_sort(lista_test))


# ------------------------------------------------------------------------

# 2. WYSZUKIWANIA O(n)

# 2.1 WYSZUKIWANIE LINIOWE
# - jak sprawdzić czy dana wartość znajduje się w naszej liście? 

def linear_search(lista: list, x):
    n = len(lista)
    for i in range(n):
        if lista[i] == x:
            return i
    return -1


print(linear_search(lista_test, 3))
print(linear_search(lista_test, 20))





# 2.2 WYSZUKIWANIE BINARNE
# - działa na posortowanym zbiorze !!
# - metoda dziel i zwyciężaj
# https://www.mathwarehouse.com/programming/gifs/binary-vs-linear-search.php


def binary_search(lista: list, x):
    low = 0
    high = len(lista) -1
    mid = 0
    while low <= high:
        # 1. wyliczamy środek
        mid = (high+low)//2

        if lista[mid] > x:
            high = mid - 1
        
        elif lista[mid] < x:
            low = mid + 1
        
        else:
            return mid
    return -1

print(bubble_sort(lista_test))
print(binary_search(lista_test, 30))
print(binary_search(lista_test, 7))



# ------------------------------------------------------------------------
# ZADANIA DODATKOWE
# ZADANIE 1
# Zadaniem ucznia jest stworzenie programu, który będzie działał jak książka
# telefoniczna. Program powinien mieć następujące funkcjonalności:

#   ● Dodawanie nowego kontaktu - program powinien pytać użytkownika o imię i
#   nazwisko oraz numer telefonu i dodać te dane do listy kontaktów. Lista
#   kontaktów powinna być przechowywana w postaci listy słowników, gdzie
#   każdy słownik reprezentuje jeden kontakt.

#   ● Sortowanie kontaktów za pomocą metody sortowania bąbelkowego -
#   program powinien sortować listę kontaktów alfabetycznie według nazwisk z
#   wykorzystaniem funkcji bubble_sort.

#   ● Wyświetlanie listy kontaktów - program powinien wyświetlić listę kontaktów
#   w formacie: "imię nazwisko - numer telefonu". Kontakty powinny być
#   posortowane alfabetycznie według nazwisk.









# ------------------------------------------------------------------------

# ZADANIE 2
# Zadaniem ucznia jest napisanie programu, który losuje liczbę z zakresu od 1 do
# 100, a następnie komputer będzie zgadywał tę liczbę, a my będziemy mu udzielać
# podpowiedzi w postaci "za mało" lub "za dużo" w zależności od tego, czy
# zgadnięta liczba jest mniejsza czy większa od wylosowanej liczby.

# Komputer będzie korzystał z algorytmu binary search, a program zakończy się, gdy
# komputer zgadnie liczbę.

# * Rekurencja - proces wywoływania funkcji przez samą siebie. 
# 
# W tym konkretnym kodzie, funkcja binary_search można zastosować rekurencje.
# Funkcja sortowania binarnego może być rekurencyjna
# będzie wywoływać samą siebie w dwóch warunkach:
# - kiedy odpowiedź jest "za mało",
# - kiedy odpowiedź jest "za dużo".
# Proces rekurencyjny trwa tak długo, aż odpowiedź jest "tak",
# wtedy funkcja zwraca wartość guess.












# ------------------------------------------------------------------------
# PODSUMOWANIE:
#   ● Wyszukiwanie binarne - podziaŁ uporządkowanej listy na połowy i
#   iteracyjnE przeszukiwaniE jednej z nich w poszukiwaniu szukanej wartości.

#   ● Sortowanie bąbelkowe - porównywaniE sąsiednich elementów listy
#   i zamianie ich kolejności, jeśli są w niewłaściwej kolejności.

# Pytania powtórzeniowe:
#   ● W jaki sposób działa wyszukiwanie binarne?
#   ● Jak działa sortowanie bąbelkowe?
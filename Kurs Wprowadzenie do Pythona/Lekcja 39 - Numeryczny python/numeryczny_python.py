# NumPy - Numerical Python

# - tablice wielowymiarowe (miacierze) [ndarray = N-Dimensional Array]
# - dużo złożonych funkcji matematycznych
# - operacje na duzych zbiorach danych
# - szybkość - zoptymalizowane operacje (oparte na językach niższego poziomu)
# - !tablice szybsze od list!


# 1. Tablica vs Lista

# 2. Ćwiczenia
import numpy as np


# Zadanie 1
# Stwórz funkcję print_array() w której zaimplementowana zostanie dwuwymiarowa
# tablica oraz wyświetlone zostaną:
# a)Tablica    [[-1,   2,  -3] 
#               [ 4,   5,   6]
#               [ 7,   8,   9]]

# b)Pierwszy wiersz tablicy
# c)Pierwszy zagnieżdżony element tablicy
# d)Typ utworzonego obiektu
# e)Kształt utworzonego obiektu
# Funkcja powinna zwracać utworzoną tablicę.

def print_array():
    tablica = np.array([[-1,   2,  -3], [ 4,   5,   6], [ 7,   8,   9]])
    print(f"Tablica:\n {tablica}")
    print(f"Pierwszy wiersz:\n {tablica[0]}")
    print(f"Pierwszy zagnieżdżony element tablicy:\n {tablica[0][0]}")
    print(f"Typ:\n {type(tablica)}")
    print(f"Kształt: {tablica.shape}")
    return tablica

arr = print_array()

# ------------------------------------------------------------------------------------
# Zadanie 2
# Stwórz funkcję shapeshifter która przyjmuje jako argument utworzoną wcześniej
# tablicę. 
# Funkcja powinna:
# a)Zmienić rozmiar tablicy na 9x1
# b)Zmienić rozmiar tablicy na 1x9
# c)Zmienić rozmiar tablicy na 3x3
# d)Zmienić rozmiar tablicy na -1x9
# e)Zmienić rozmiar tablicy na 3x-1
# f)Podzielić tablicę na 3 nowe tablice
print("\n\n\n")

# '-1' : wstawiamy kiedy nie wiemy ile i komputer liczby sam
# (wiersze, kolumny)
# (ile_'list', ile_elementów_w_'liście')


def shapeshifter(tablica):
    print(f"Rozmiar  9 x 1:\n{tablica.reshape(9,1)}")
    print(f"Rozmiar  1 x 9:\n{tablica.reshape(1,9)}")
    print(f"Rozmiar  3 x 3:\n{tablica.reshape(3,3)}")
    print(f"Rozmiar -1 x 9:\n{tablica.reshape(-1,9)}")
    print(f"Rozmiar  3 x-1:\n{tablica.reshape(3,-1)}")
    nowa_tab = np.array_split(tablica.reshape(-1,9), 3)
    print(f"Nowe:\n {nowa_tab}")

shapeshifter(arr)

# ------------------------------------------------------------------------------------
# Zadanie 3
# Utwórz funkcję data_format, która zawierać będzie tablicę zawierającą dane
# różnych typów - wcześniej wspomniane zostało że tablice mogą przechowywać dane
# tylko 1 typu, dlatego należy obsłużyć ewentualny wyjątek. Dodatkowo utwórz tablice
# w których dane rzutowane będą kolejno na stringi, inty i floaty.

# dtype = ...
# | Kategoria | Zalecany `dtype` | Kod literowy | Opis                                      |
# | --------- | ---------------- | ------------ | ----------------------------------------- |
# | Integer   | `int64`          | `'i'`, `'u'` | Liczby całkowite (ze znakiem / bez znaku) |
# | Float     | `float64`        | `'f'`        | Liczby zmiennoprzecinkowe                 |
# | Boolean   | `bool`           | `'?'`        | Wartości logiczne                         |
# | Complex   | `complex128`     | `'c'`        | Liczby zespolone                          |
# | String    | `str` / `'U'`    | `'U'`        | Napisy Unicode                            |
# | Daty      | `datetime64`     | `'M'`        | Daty i czas                               |
# | Czas      | `timedelta64`    | `'m'`        | Różnice czasu                             |
# | Obiekty   | `object`         | `'O'`        | Dowolne obiekty Pythona                   |

# [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]] - do zmiany formatu
print("\n\n\nzadanie3:")

def data_format():
    try:
        tablica = np.array([[1.1 , 2.2 ,3.3], ['kot', 12, 'olaf'], ['a', 'b', '5']])
        print(tablica)
        print(type(tablica[0][0]))
    except Exception as e:
        print(e)

    print("Ćwiczenia:\n")
    arr = np.array([[1.1, 2.2, 3.3], [4.4 , 5.5 , 6.6], [7.7 , 8.8 , 9.9]], dtype='i')
    print(arr)
    print(type(arr[0][0]))


data_format()


# ------------------------------------------------------------------------------------
# Zadanie 4
# Utwórz funkcję sorted_ndarray w której utworzona zostanie tablica, a następnie
# wyświetlona, oraz posortowana i ponownie wyświetlona.

def sorted_ndarray():
    tablica = np.array([[2, 6, 2], [8, 2, 28], [4, 4, 8]])
    print(f"Tablica przed sortowaniem:\n {tablica}")
    print(f"Tablica po sortowaniu:\n {np.sort(tablica)}")

sorted_ndarray()


# ------------------------------------------------------------------------------------
# Zadanie 5
# Stwórz funkcję generate_random_numbers która wygeneruje 10 losowych liczb
# całkowitych od 0 do 100, oraz 10 losowych liczb typu float z zakresu od 0 do 1.
print("\n\n\n")







# ------------------------------------------------------------------------------------
# Zadanie 6
# Stwórz funkcję pick_random_numbers która:
# a) wygeneruje tablicę losowych liczb z zakresu od 0 do 1 o wymiarach 3x5.
# b) wybierze losową liczbę ze zbioru liczb 3,5,7,9
# c) utworzy tablicę o wymiarach 3x5 z losowych elementów ze zbioru liczb 3,5,7,9
# d) wygeneruj 100 losowych liczb, korzystając ze zbioru liczb 3,5,7,9, 
# gdzie szansa na: 3 wynosi 10%, na 5-30 %, na 7-60%, a na 9-0%.
print("\n\n\n")







# ------------------------------------------------------------------------------------
# Zadanie 7
# Stwórz funkcję shuffle_ndarray w której przemieszasz tablicę oraz utworzysz
# permutację tablicy.
print("\n\n\n")







# shuffle - tasuje oryginalną tablicę
# permutacja - tworzy nową pomieszaną tablicę z podanej


# ------------------------------------------------------------------------------------
# Zadanie 8
# Stwórz funkcję array_functions w której:
# a)Wygenerujesz tablicę z 11 wartościami równo rozmieszczonymi na przedziale od 0 do 10
# b)Wyświetlisz tą tablicę
# c)Wyświetlisz sumę elementów tej tablicy
# d)Wyświetlisz najmniejszy element tablicy
# e)Wyświetlisz największy element tablicy
# f) Wyświetlisz średnią wartość tablicy
# g)Wyświetlisz wariancje elementów tablicy (jak daleko, przeciętnie, elementy są od średniej)
# (https://pogotowiestatystyczne.pl/slowniki/wariancja/)
# h)Wyświetlisz odchylenie standardowe elementów tablicy (typowa odległość od średniej)
# (https://pogotowiestatystyczne.pl/slowniki/odchylenie-standardowe/)
print("\n\n\n")







# ------------------------------------------------------------------------------------
# Zadanie 9
# Utwórz funkcję mathematical_functions w której:
# a)Wyświetlisz wartość liczby pi
# b)Wyświetlisz wartość liczby eulera
# c)Wyświetlisz wartość kwadratu liczby eulera
# d)Wyświetlisz wartość sinus pi/2
# e)Wyświetlisz wartość cosinus pi/2
# f)Wyświetlisz wartość tangens pi/2
# g)Wyświetlisz wartość pi/2 zamienioną na stopnie i 360 stopni zamienioną na radiany.
print("\n\n\n")





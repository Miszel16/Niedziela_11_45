#https://github.com/Miszel16/Niedziela_11_45


#Zadanie "Dzielenie"
# Napisz funkcję, która otrzyma dwa argumenty pierwszym będzie liczba, którą chcemy
# podzielić bez reszty a drugim argumentem będzie dzielnik. Należy sprawdzić czy
# można dokonać dzielenia a jeśli tak zwrócić informację czy liczba jest podzielna bez reszty czy nie.

def dzielenie(dzielna: int, dzielnik: int) -> str:
    if dzielnik == 0:
        return "Nie można dzielić przez 0."

    if dzielna % dzielnik == 0:
        return f"Liczba {dzielna} jest podzielna całkowicie przez {dzielnik}."
    else:
        return f"Liczba {dzielna} nie jest podzielna całkowicie przez {dzielnik}."

# print(dzielenie(7, 0))
# print(dzielenie(7, 2))
# print(dzielenie(8, 2))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#TYPE HINTING

# def prostokat(a: float, b: float) -> float:
#     obwod = 2*a + 2*b
#     return obwod

# wynik = prostokat(4.6, 6.8)
# print(wynik)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Szablon osoby"
# Napisz funkcję, która przyjmuje następujące argumenty:
# imie (str), wiek (int), wzrost_m (float), 
# a zwraca napis: “Jan, lat 20, 1.75 m wzrostu” - oczywiście argumenty należy podstawić do szablonu. 
# * Wzrost ma zawsze pokazywać dwa miejsca po przecinku.

# def szablon(imie: str, wiek: int, wzrost_m: float) -> str:
#     return f"{imie}, lat {wiek}, {wzrost_m} wzorstu"

# print(szablon("Alicja", 20, 1.75))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Unikalna lista"
# Napisz funkcję, która jako argument otrzymuje listę elementów, w której mogą
# występować powtórzenia, a zwraca listę unikalnych elementów.
# elem in lista
# Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5]

def unikalna_lista(lista: list) -> list:
    wynik = []
    for elem in lista:
        if not elem in wynik:
            wynik.append(elem)
    return wynik

print(unikalna_lista([1,2,3,3,3,3,4,5]))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Suma cyfr"
# Napisz funkcję, która otrzymuje liczbę całkowitą, a zwraca sumę jej cyfr.
# Dla liczby 249 otrzymujemy 2+4+9 czyli 15

#string to lista znaków

def suma_cyfr(liczba: int) -> int:
    suma = 0
    liczba = abs(liczba)
    while liczba > 0:
        suma = suma + liczba % 10
        liczba = liczba // 10
    return suma

suma = (suma_cyfr(249))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Liczby losowe"
# Napisz funkcję, która zwraca listę losowych liczb. Rozmiar listy zależy od argumentu.
# Dodatkowo: Funkcja powinna otrzymać dwa dodatkowe argumenty: minimalna i
# maksymalna wartość, która może zostać wylosowana.
import random

liczba_random = random.randint(0, 8) #losowane liczby: <0;8>




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Logowanie"
# Napisz funkcję, która zapyta użytkownika o hasło i login. Funkcja ma zwrócić 'True', jeśli
# podano poprawne hasło i login lub 'False' w innym przypadku.


# Zadanie "Logowanie z określoną liczba prób"
# Wykorzystaj powyższą funkcję w funkcji, która pozwala na 'n' prób logowań.
# Zwraca 'True' jeśli udało się zalogować lub 'False' jeśli przekroczono liczbę prób.
# Funkcja również musi przyjmować poprawne hasło i login.
# Wprowadzenie niepoprawnej wartości 'n' powinno zostać obsłużone (zapytanie
# jednorazowe dla takich przypadków) - czyli jeśli n < 1 to przyjmujemy, że n=1.
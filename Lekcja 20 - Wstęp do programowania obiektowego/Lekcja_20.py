# 1. Zadanie - Problem
# Napisz program, który:
#   - Zapisze dane czterech osób (imiona, nazwiska i wiek) w zmiennych.
#   - Wypisze ich imię i nazwisko.
#   - Sprawdzi, czy dana osoba jest pełnoletnia (wiek ≥ 18),
#     czy niepełnoletnia, i wypisze odpowiedni komunikat.
# Spróbuj to zrobić dla wszystkich czterech osób.

#    nazwa pliku        nazwa klasy
from Uzytkownicy import Uzytkownik # importowanie klasy

# tworzenie obiektów
user1 = Uzytkownik()
user2 = Uzytkownik()
user3 = Uzytkownik()
user4 = Uzytkownik()


# nadanie wartosci atrybutom
user1.imie = "Alicja"
user1.nazwisko = "Kowalska"
user1.wiek = 15

user2.imie = "Wojtek"
user2.nazwisko = "W"
user2.wiek = 20

user3.imie = "Piotr"
user3.nazwisko = "P"
user3.wiek = 18

user4.imie = "Patrycja"
user4.nazwisko = "D"
user4.wiek = 9

#print(user1.imie, user1.nazwisko, user1.wiek)

user1.czy_pelnoletni()
user2.czy_pelnoletni()
user3.czy_pelnoletni()
user4.czy_pelnoletni()

print()
print(user3.imie, user3.nazwisko, user3.wiek)

user3.zmien_wiek(14)
print(user3.imie, user3.nazwisko, user3.wiek)
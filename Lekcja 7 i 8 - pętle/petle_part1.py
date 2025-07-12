# https://github.com/Miszel16/Niedziela_11_45

#Czym jest pętla? Co nam daje używanie pętli?



# PĘTLA WHILE
# wykonuje się dopóki warunke jest spełniony
# wynik_warunku = False


# while wynik_warunku:
#     print("Warunek jest spełniony")
#     print("thftgadfg")

# Korzyści korzystania z pętli:
# 1. Znacznie mniej linijek do napisania
# PRZYKŁAD - chcemy przywitać się 10 razy

#bez pętli:
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")

#z pętlą
# i=0
# while i<100:
#     print("Dzień dobry")
#     i+=1
# print("hejka")

# #2. Elastyczny kod
# #PRZYKŁAD - chcemy przywitać się jednak 25 razy

# #3. Czytelność kodu

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #Zadanie 1 "Wyświetlanie komunikatów"
# #Program wypisze tyle przywitac ile nakaże mu użytkownik

# liczba = int(input("Podaj liczbe: "))

# i=0
# while i<liczba:
#     print(". Hejka")
#     i += 1
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# #Zadanie 2 "Timer bomby"
#Program wykonuje odliczanie od podanej przez użytkownika liczby
#Następnie pojawia się napis "BOOM!"
import time #praca z czasem
time.sleep(1) #sekundy

# liczba = int(input("Podaj liczbę do odliczania: "))

# while liczba > 0:
#     print({liczba})
#     time.sleep(1)
#     liczba -= 1

# print("BOOM!")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #Zadanie 3 "Zgadywanka"
# #Zgadujemy liczbę jaką wylosował komputer
# #Program, dopóki nie zgadniemy, daje nam odpowiedzi "za dużo", "za mało", lub "ZGADŁEŚ" jest uda nam się zgadnąć
# import random #losowanie wartości
import random

# wylosowana_liczba = random.randint(0, 100) #od 0 do 100 włącznie

# odpowiedz = None

# while odpowiedz != wylosowana_liczba:
#     odpowiedz = int(input("Zgadnij: "))
#     if odpowiedz < wylosowana_liczba:
#         print("Za mało")
#     elif odpowiedz > wylosowana_liczba:
#         print("Za dużo")
#     else:
#         print(f"ZGADŁAŚ! Wylosowana liczba to {odpowiedz}")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#PĘTLA NIESKOŃCZONA
#przydatna np. do stacji pogodowych
import time

# while True:
#     print("Nie zatrzymam się")
#     time.sleep(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#BREAK - przerwij pętle 
# import time
# i=0
# while True:
#     i+=1
#     if i==3:
#         break
#     print(f"{i}")

# print("Żart, jednak się zatrzymam")

#PRZYKŁAD
# Zadanie "Echo"

# print("Będe twoim echem")

# while True:
#     odp = input("Napisz slowo: ")
#     if odp=="exit":
#         break
#     print("Echo: " + odp)

# print("Do zobaczenia")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#CONTINUE - pomiń ten krok i przejdź do następnego, czyli zakończ ten obrót pętli i sprawdź warunek od nowa

#PRZYKŁAD
# i=0
# while True:
#     if i == 10:
#         break
#     if i==5:
#         i+=1
#         continue
#     i+=1
#     print(i)
#     time.sleep(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie "Logowanie"
#Użytkownik musi podać poprawnie po kolei: PIN, rok_urodzenia, haslo
#Jeżeli jakiekolwiek dane zostaną podane źle, program zaczyna się od nowa
#Dopiero jeśli wszytskie dane zostaną podane poprawnie to pętla się kończy i daje komunikat o zalogowaniu

PIN = "4321"
ROK_URODZENIA = "2005"
HASLO = "1234"

#1. Prośba o pin
#2. Sprawdz czy jest zły
    #2a. continue
#3. Prośba o rok urodzenia
#4. Sprawdz czy jest zły
    #4a. continue
#5. Prośba o hasło
#6. Sprawdz czy jest złe
    #6a. continue
#7. Zalogowano! - break

# while True:
#     pin = input("Podaj PIN: ")
#     if pin != PIN:
#         print("Odmowa dostępu")
#         continue

#     rok_urodzenia = input("Podaj rok uroczenia: ")

#     if rok_urodzenia != ROK_URODZENIA:
#         print("Odmowa dostępu")
#         continue

#     haslo = input("Podaj hasło: ")

#     if haslo != HASLO:
#         print("Odmowa dostępu")
#         continue

#     print("Zalogowano pomyślnie!")
#     break

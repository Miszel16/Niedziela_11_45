# https://www.giganciprogramowania.edu.pl/kursy/433-wstep-do-programowania-w
# -pythonie-semestr-2-online?kind=Semestralne+kursy+online

# Zadania powtórzeniowe


# Zadanie 1 – FizzBuzz
# Celem zadania FizzBuz jest napisanie programu, który wypisze na ekranie liczby 1 do 100,
# - zamiast liczb podzielnych przez 3 ma napisać Fizz,
# - zamiast podzielnych przez 5 Buzz,
# - zamiast podzielnych przez 3 i 5 FizzBuzz.

# start, stop, step
# for i in range(1, 101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



# Zadanie 2 - wzór
# Napisz program, który wyświetli na ekranie ten wzór, zależnie od liczby jaką podamy:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

# liczba = int(input("Podaj liczbę: ")) # 4

# # start, stop, step
# for i in range(1, liczba+1): # i = 2
#     for a in range(i): #2
#         print(i, end=" ")
#     print()





# Zadanie 3 – min i max
# Należy napisać program, który z listy pokaże nam najmniejszą i największą liczbę

# lista = [1, 3, 7, 11, 2, -6, 0]
# # min(), max() - nie korzystamy

# najmniejsza = lista[0]
# najwieksza = lista[0]

# for i in lista:
#     if i < najmniejsza:
#         najmniejsza = i
#     if i > najwieksza:
#         najwieksza = i



# print(f"Największa wartość to {najwieksza}")
# print(f"Najmniejsza wartość to {najmniejsza}")










# Zadanie 4 – zliczanie liter
# Program ma zliczyć ile danych liter znajduje się w zdaniu
# Przykładowe wyświetlanie:
# "ABC przykladowy tekst na potrzeby naszego programu"

# Slowa: 7, Litery: 44, ilosc liter: {'a': 5, 'b': 2, 'c': 1, 'p': 3, 'r': 4, 'z': 3, 'y': 3,
#  'k': 2, 'l': 1, 'd': 1, 'o': 4, 'w': 1, 't': 3, 'e': 3, 's': 2, 'n': 2, 'g': 2, 'm': 1, 'u': 1}

# tekst = "ABC przykladowy tekst na potrzeby naszego programu"

# slowa = 0
# litery = 0
# slownik = {}

# for slowo in tekst.split(" "):
#     slowa += 1
#     for znak in slowo:
#         znak = znak.lower()
#         litery += 1
#         if znak in slownik:
#             slownik[znak] += 1
#         else:
#             slownik[znak] = 1

# print(f"Słowa: {slowa}")
# print(f"Litery: {litery}") 
# print(slownik)








# Zadanie 5 – orzeł i reszka
# Gracz będzie zgadywać co wypadnie następne, i punkty będzie dostawać albo gracz, albo komputer.



# KOD BINARNY = SYSTEM DWÓJKOWY

# 🔘 system dziesiętny:
# - 10 cyfr: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# 🔘 system dwójkowy:
# - w cyfr: 0, 1

# Jak przeliczyć z dziesiętnego na binarny?

# 19 (s. 10) -> 10011 (s. 2)

# dzielenie | reszta
# 19 : 2    | 1       (19/2 = 9)
# 9 : 2     | 1       ( 9/2 = 4)
# 4 : 2     | 0       ( 4/2 = 2)
# 2 : 2     | 0       ( 2/2 = 1)
# 1 : 2     | 1       ( 1/2 = 0)
# 0 : 2     | 0       ( 0/2 = 0)


#   1   0   0   1   1
#   2⁴  2³  2²  2¹  2⁰
#   16  8   4   2   1

# 1*2⁴ + 0*2³ + 0*2² + 1*2¹ + 1*2⁰ = 16 + 2 + 1 = 19

# PRZYKŁADY:
# - 56
# - 1 0 1 0 1


# 1 + 4 + 16 = 21



# odp
# 56₁₀ = 111000₂
# 10101₂ = 21₁₀




# Zadanie 1 (dziesiętnie -> binarnie)
# Napisz funkcję, która otrzyma jeden argument określający liczbę dziesiętną. Funkcja ma
# wyświetlić ile wynosi podana liczba w zapisie binarnym.

# def dziesietne_na_binarne(dziesietna:int) -> str:
#     binarna = ""
#     while dziesietna > 0:
#         reszta = dziesietna % 2
#         dziesietna = dziesietna // 2
#         binarna = str(reszta) + binarna
    
#     return binarna

# liczba = 56
# binarna = dziesietne_na_binarne(liczba)
# print(binarna)





# Zadanie 2 (binarnie -> dziesiętnie)
# Napisz funkcję, która otrzyma jeden argument określający liczbę binarną. Funkcja ma
# wyświetlić ile wynosi podana liczba w zapisie dziesiętnym.



# #2^5   2⁴   2³   2²   2¹  2⁰
# #---------------------------------------
# # 1    1    1    0    0    0     wartosci
# #---------------------------------------
# # 0    1    2    3    4    5     i

# len(binarna) = 6
# potega = len(binarna) - 1 - i


def binarne_na_dziesietne(binarna: str) -> int:
    dziesietna = 0
    for i, elem in enumerate(binarna):
        potega = len(binarna) - 1 - i
        wartosc = int(elem) * 2**potega
        dziesietna += wartosc
    return dziesietna

number = str(111000)

dziesietna = binarne_na_dziesietne(number)
print(dziesietna)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LICZBY PIERWSZE

# Liczba pierwsza to taka, która dzieli się przez '1' i przez samą siebie.

# liczba | dzielniki  (czy liczba pierwsza?)
#   1    |           
#   2    | 
#   3    | 
#   4    | 
#   5    | 
#   6    | 
#   7    | 
#   8    | 
#   9    | 
#   10   | 


# Zadanie 3
# Waszym zadaniem jest napisać funkcję, która zwróci informacje 'prawda/fałsz' czy
# podana liczba jest liczbą pierwszą.


# Zadanie 4
# Napisz drugą funkcję, która ma wyświetlić wszystkie liczby pierwsze z podanego
# przedziału (możesz wykorzystać do tego funkcję, którą już napisałeś)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PALINDROMY

# Palindrom to takie słowo, liczba lub zdanie, które czytane od przodu i od tyłu brzmi tak samo.

# PRZYKŁADY:

# kajak
# anna
# oko
# 1331
# 44
# 12321
# „Kobyła ma mały bok”
# „A to idiota”

# Podpowiedź i przypominajka:

# text[start:stop:step]

# start – od którego znaku zacząć (domyślnie od początku)
# stop – na którym znaku skończyć (domyślnie do końca)
# step – co ile znaków skakać (np. co 1, co 2... lub wstecz!)

# Jak są porównywane zmienne typu string?


# Zadanie 5
# Napisz funkcję, która jako argument otrzymuje tekst i sprawdzi czy jest on palindromem
# wyświetlając: „{podane słowo} jest palindromem” lub „{podane słowo} nie jest palindromem”
# *ZAAWANSOWANE* ulepszyć program, tak aby ignorował wielkość liter 
# (podpowiedź: Wykorzystajcie metodę toUpper lub toLower)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ANAGRAMY

# Anagram to nowe słowo (lub zdanie), które powstaje przez przestawienie liter innego słowa.
# Litery są te same, tylko ułożone w innej kolejności.

# PRZYKŁADY:

# kot → tok, okt
# lama → mala, alma
# roma → amor
# nos → son


# Zadanie 6
# Napisz funkcję, która sprawdzi czy dwa podane wyrazy są anagramami



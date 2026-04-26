def add(a,b):
    return a+b

# Zadanie 1. Palindrom 
# Napisz funkcję sprawdzającą czy dane słowo jest palindromem (palindrom to 
# słowo które pisane od przodu i od tyłu jest identyczne). 
# Napisz testy, które sprawdzą, czy słowa “kamilslimak” i “ala” są palindromami, a 
# słowa “wiadro” i “kamyk” nimi nie są.

def if_palindrom(word):
    return word == word[::-1] # True/False
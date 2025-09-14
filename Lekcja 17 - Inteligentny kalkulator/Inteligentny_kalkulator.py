# 1. Pobierz tekst 
# 2. Przetłumacz tekst "111+170"
# 3. Zmień na liczby 
# 4. Oblicz wynik

# Etap 1
zero = ["0", "zero", "zerem", "zera"] # baza_symbolu
jeden = ["1", "jeden", "jedynka", "jedynkę"] # baza_symbolu
plus = ["+", "plus", "dodać", "dodaj"] # baza_symbolu
baza = [zero, jeden, plus] # baza

# FUNKCJE
def przetlumacz(slowo: str) -> str: # "jeden"
    for baza_symbolu in baza:
        # 1. rozwiązanie
        if slowo in baza_symbolu:
            return baza_symbolu[0]
        # 2. rozwiązanie
        # for symbol_z_bazy in baza_symbolu:
        #     if symbol_z_bazy == slowo:
        #         return baza_symbolu[0]
    return " "
    

def oblicz(liczba1: int, znak: str, liczba2: int) -> int:
    # +, -, *, /
    if znak == "+":
        return liczba1 + liczba2
    elif znak == "-":
        return liczba1 - liczba2
    elif znak == "*":
        return liczba1 * liczba2
    elif znak == "/":
        if liczba2 == 0:
            return "Nie można dzielić przez zero"
        else:
            return liczba1 / liczba2
    else:
        return "Niepoprawny znak"



def oblicz_z_tekstu(dzialanie_tekst: str) -> int: #" + "
    liczba1 = "" #"111"
    liczba2 = ""
    znak = ""

    for i in dzialanie_tekst:
        if i.isdigit():
            if znak == "":
                liczba1 += i
            else:
                liczba2 += i
        else:
            znak = i

    if liczba1 == "" or liczba2 == "" or znak == "":
        return "Nie rozumiem działania - sprawdź słowa."

    liczba1 = int(liczba1)
    liczba2 = int(liczba2)

    return oblicz(liczba1, znak, liczba2)


tekst = input("Podaj swoje równanie: ") #str
# "jeden jeden jeden dodać jeden siedem zero"

dzialanie = "" #str


# while - wykonuje się dopóki warunek jest spełniony
# for - wykonuje się z góry okresloną ilość razy
for slowo in tekst.split(" "):
    przetlu_slowo = przetlumacz(slowo)
    dzialanie += przetlu_slowo

print(dzialanie)
print(oblicz_z_tekstu(dzialanie))

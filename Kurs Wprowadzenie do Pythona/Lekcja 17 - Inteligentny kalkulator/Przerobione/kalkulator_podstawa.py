# Pięć dodać siedem -> 5 + 7 = 12

#ETAP 1

# 1. Baza słów kluczowych
zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynka", "jedynkę"]
plus = ["+", "plus", "dodać", "dodaj"]
baza = [zero, jeden, plus]


# 2. Przyjęcie polecenia od użytkownika
tekst = input("Podaj tekst: ")

# 3. Zmienna odpowiedzialna za przetłumaczone działanie
dzialanie = ""


# 5. Funkcja tłumacząca słowa
def przetlumacz(slowo):
    for baza_symbolu in baza:
        for slowo_bazy_symbolu in baza_symbolu:
            if slowo == slowo_bazy_symbolu:
                return baza_symbolu[0] # pierwszy element danej bazy, który jest symbolem
    return ''


# 4. Rozdzielenie pobranego tekstu na osobne słowa
for slowo in tekst.split(" "):
    slowo_przetlumaczone = przetlumacz(slowo)
    dzialanie += slowo_przetlumaczone
print(dzialanie)

#-------------------TESTY-------------------
#jeden jeden jeden plus jeden jeden zero  ->  111+110

#ETAP 2

# 1. Wybrana operacja oraz wynik
def oblicz(liczba1, liczba2, znak):
    if znak == '+':
        return liczba1 + liczba2
    elif znak == '-':
        return liczba1 - liczba2
    elif znak == '*':
        return liczba1 * liczba2
    elif znak == '/':
        if liczba2 != 0:
            return liczba1 / liczba2
        else:
            return "Nie można dzielić przez zero"
    

# 2. Przekształcenie tekstu z działaniem w działanie matematyczne
def oblicz_z_tekstu(dzialanie_tekst):
    # musimy rozdzielić tekst na słowa zawierające liczby oraz znak
    liczba1 = ''
    liczba2 = ''
    znak = ''

    for i in dzialanie_tekst:
        if i.isdigit():
            if znak == "":
                liczba1 += i
            else:
                liczba2 += i
        else:
            znak = i

    if liczba1 == "" or liczba2 == "" or znak == "":
        return "Nie rozumiem działania — sprawdź słowa."
    
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)
    
    return oblicz(liczba1, liczba2, znak)
            
print(oblicz_z_tekstu(dzialanie))

#-------------------TESTY-------------------
#jeden jeden jeden plus jeden jeden zero  ->  111+110 = 221
#jeden pięć zero dodać dwa  ->  10+ = Nie rozumiem działania — sprawdź słowa.

#ETAP 3
# 1. Zwiększenie bazy danycyh (0-19)
# dwa = ["2", "dwa", "dwójkę", "dwójka"]
# trzy = ["3", "trzy", "trójkę", "trójka"]
# cztery = ["4", "cztery", "czwórkę", "czwórka"]
# piec = ["5", "pięć", "piątkę", "piątka"]
# szesc = ["6", "sześć", "szóstkę", "szóstka"]
# siedem = ["7", "siedem", "siódemkę", "siódemka"]
# osiem = ["8", "osiem", "ósemkę", "ósemka"]
# dziewiec = ["9", "dziewięć", "dziewiątkę", "dziewiątka"]
# dziesiec = ["10", "dziesięć", "dziesiątka", "dziesiątkę", "dychę"]
# jedenascie = ["11","jedenaście", "jedenastkę", "jedenastu"]
# dwanascie = ["12", "dwanaście", "dwunastu", "dwunastkę"]
# trzynascie = ["13", "trzynaście","trzynastu","trzynastkę"]
# czternascie = ["14", "czternaście", "czternastu", "czternastkę"]
# pietnascie = ["15", "piętnaście","piętnastu", "piętnastkę"]
# szesnascie = ["16", "szesnaście","szesnastu","szesnastkę"]
# siedemnascie = ["17","siedemnaście", "siedemnastu", "siedemnastkę"]
# osiemnasice = ["18", "osiemnaście","osiemnastu","osiemnastkę"]
# dziewietnascie = ["19","dziewiętnaście", "dziewiętnastu","dziewiętnastkę"]

# minus = ["-", "odejmij", "minus", "odjąć"]
# gwiazdka = ["*", "x", "razy", "mnożone", "pomnożone", "pomnożyć"]
# ukosnik = ["/", ":", "dzielone", "podziel"]
# baza = [zero, jeden,dwa,trzy, cztery, piec, szesc,siedem, osiem, dziewiec,dziesiec,
#         jedenascie,dwanascie,trzynascie,czternascie,pietnascie,szesnascie,siedemnascie,
#         osiemnasice,dziewietnascie, plus, minus, gwiazdka, ukosnik]

#-------------------TESTY-------------------
# jedenaście plus trzy dzielone przez dwójkę  ->  11+3/2 = 0.34375
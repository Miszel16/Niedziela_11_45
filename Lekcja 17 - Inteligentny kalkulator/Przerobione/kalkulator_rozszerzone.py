# Obsługa liczb 20 - 99, czyli jak zrobić cześci dziesiętne?

zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynka", "jedynkę"]
dwa = ["2", "dwa", "dwójkę", "dwójka"]
trzy = ["3", "trzy", "trójkę", "trójka"]
cztery = ["4", "cztery", "czwórkę", "czwórka", "czter"]
piec = ["5", "pięć", "piątkę", "piątka"]
szesc = ["6", "sześć", "szóstkę", "szóstka"]
siedem = ["7", "siedem", "siódemkę", "siódemka"]
osiem = ["8", "osiem", "ósemkę", "ósemka"]
dziewiec = ["9", "dziewięć", "dziewiątkę", "dziewiątka"]
dziesiec = ["10", "dziesięć", "dziesiątka", "dziesiątkę", "dychę"]
jedenascie = ["11","jedenaście", "jedenastkę", "jedenastu"]
dwanascie = ["12", "dwanaście", "dwunastu", "dwunastkę"]
trzynascie = ["13", "trzynaście","trzynastu","trzynastkę"]
czternascie = ["14", "czternaście", "czternastu", "czternastkę"]
pietnascie = ["15", "piętnaście","piętnastu", "piętnastkę"]
szesnascie = ["16", "szesnaście","szesnastu","szesnastkę"]
siedemnascie = ["17","siedemnaście", "siedemnastu", "siedemnastkę"]
osiemnasice = ["18", "osiemnaście","osiemnastu","osiemnastkę"]
dziewietnascie = ["19","dziewiętnaście", "dziewiętnastu","dziewiętnastkę"]

plus = ["+", "plus", "dodać", "dodaj", "dodac"]
minus = ["-", "odejmij", "minus", "odjąć"]
gwiazdka = ["*", "x", "razy", "mnożone", "pomnożone", "pomnożyć"]
ukosnik = ["/", ":", "dzielone", "podziel"]
baza = [zero, jeden,dwa,trzy, cztery, piec, szesc,siedem, osiem, dziewiec,dziesiec,
        jedenascie,dwanascie,trzynascie,czternascie,pietnascie,szesnascie,siedemnascie,
        osiemnasice,dziewietnascie, plus, minus, gwiazdka, ukosnik]


# 1. Jakie są końcówki dziesiątek?
dziesiatki = ["dzieścia", "dziesiąt", "dzieści"]

# 2. Zmienna pomocnicza: czy należy dodać zero do liczby? (czterdzieści [40] jeden [41])
# - '<0' : nie było liczby z zakresu 20-99
# - '0' : oczekujemy liczby jedności
# - '1' : obecna liczba ma końcówkę 'dziesiąt'
dziesietna_liczba = -1













# 3. Modyfikacja funkcji 'przetlumacz()'

def przetlumacz(slowo):
    global dziesietna_liczba #można modyfikować zmienną, która została utworzona poza funkcją
    for koncowka in dziesiatki:
        if slowo.endswith(koncowka):
            dziesietna_liczba = 1
            slowo = slowo.replace(koncowka,'')

    for baza_symbolu in baza:
        for slowo_bazy_symbolu in baza_symbolu:
            if slowo == slowo_bazy_symbolu:
                if dziesietna_liczba == 0 and not(baza_symbolu[0].isdigit()):
                    dziesietna_liczba = -1
                    return "0" + baza_symbolu[0]
                else:
                    dziesietna_liczba = dziesietna_liczba - 1
                    return baza_symbolu[0]
    return ''

# PRZYKŁAD: "czterdzieści dodać"
# 1. pierwsza pętla: "czter"
#    druga pętla: "4"
# 2. pierwsza pętla: "dodać"
#    druga pętla: "0" + "+"
# wynik: 40+


#-------------------4 punkt w pętli-------------------

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











def oblicz_z_tekstu(dzialanie_tekst):
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

# 4. Jeśli ostatnia liczba jest z zakresu (20-99) to musimu obsłużyć to w pętli

kontynuowanie = ""
while kontynuowanie != "n":
    dzialanie = ""
    tekst = input("Podaj tekst: ").lower()

    for slowo in tekst.split(" "):
        slowo_przetlumaczone = przetlumacz(slowo)
        dzialanie += slowo_przetlumaczone

    if dziesietna_liczba == 0:
        dzialanie+="0"
        dziesietna_liczbaa = -1

    print(dzialanie)
         
    print(oblicz_z_tekstu(dzialanie))
    kontynuowanie = input("Czy chcesz kontynuować działanie programu (t/n)?").lower()

print("Koniec")

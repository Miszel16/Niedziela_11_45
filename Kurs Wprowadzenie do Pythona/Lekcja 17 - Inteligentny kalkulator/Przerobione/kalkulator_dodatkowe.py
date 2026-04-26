# Wielokrotne działanie programu oraz ignorowanie wielkich liter

zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynka", "jedynkę"]
dwa = ["2", "dwa", "dwójkę", "dwójka"]
trzy = ["3", "trzy", "trójkę", "trójka"]
cztery = ["4", "cztery", "czwórkę", "czwórka"]
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

plus = ["+", "plus", "dodać", "dodaj"]
minus = ["-", "odejmij", "minus", "odjąć"]
gwiazdka = ["*", "x", "razy", "mnożone", "pomnożone", "pomnożyć"]
ukosnik = ["/", ":", "dzielone", "podziel"]
baza = [zero, jeden,dwa,trzy, cztery, piec, szesc,siedem, osiem, dziewiec,dziesiec,
        jedenascie,dwanascie,trzynascie,czternascie,pietnascie,szesnascie,siedemnascie,
        osiemnasice,dziewietnascie, plus, minus, gwiazdka, ukosnik]


def przetlumacz(slowo):
    for baza_symbolu in baza:
        for slowo_bazy_symbolu in baza_symbolu:
            if slowo == slowo_bazy_symbolu:
                return baza_symbolu[0]
    return ''

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


kontynuowanie = ""
while kontynuowanie != "n":
    dzialanie = ""
    tekst = input("Podaj tekst: ").lower()

    for slowo in tekst.split(" "):
        slowo_przetlumaczone = przetlumacz(slowo)
        dzialanie += slowo_przetlumaczone
    print(dzialanie)
         
    print(oblicz_z_tekstu(dzialanie))
    kontynuowanie = input("Czy chcesz kontynuować działanie programu (t/n)?").lower()

print("Koniec")

# Tabela z wynikami dla jednego gracza
# Gra trwa dopóki wszystkie rubryki nie będa pełne

# PLAN OGÓLNY:
# 1. Rzucamy wybranymi kośćmi (pierwszy rzut - wszytskie)  [+]
# 2. Wyświetlenie co wyrzuciliśmy   [+]
# 3. Czy chcemy rzucać jeszcze raz?   [+]
# 4. Ponowny rzut wybranymi kości (max. 2)   [+]
# 5. Wyświetlenie tabeli [+]
# 6. Gdzie chcemy wpisać punkty? [+] 
# 7. Wstawienie punktów do odpowiedniej rubryki [+]
# * gra wykonuje się tyle razy ile jest rubryk w tabeli (pętla)

import random
kosci = [0, 0, 0, 0, 0]
#        0, 1, 2, 3, 4

kategorie = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątka", "Szóstki"]
punkty = ['','','','','','']



def rzut_koscmi(numery_kosci: str): #"12345" - iterowanie
    for i in numery_kosci:
        index = int(i) # zmiana str -> int
        index = index - 1
        kosci[index] = random.randint(1, 6)



def pokaz_kosci():
    print("______________")
    for i in range(1, len(kosci)+1):  #1,2,3,4,5
        print(f"    {i}. {kosci[i-1]}")
    print("______________")



def sprawdz_czy_przerzut() -> bool:
    odp = input("Czy chcesz przerzucić któreś z kości? (t/n)").lower() # .lower() - robi małe literki z dużych
    if odp == 't':
        return True
    else:
        return False
    

def pokaz_tabele_punktow():
    pierwszy_wiersz = ""
    drugi_wiersz = ""
    
    for i in range(len(kategorie)):
        pierwszy_wiersz += str(i+1) + '. ' + kategorie[i] + ' | '
        drugi_wiersz += str(punkty[i]).center(len(kategorie[i]) + 3) + ' | '
    
    print("__________________________________________________________________________")
    print(pierwszy_wiersz)
    print("--------------------------------------------------------------------------")
    print(drugi_wiersz)
    print("__________________________________________________________________________")


def punkty_w_szkole(pole: int):
    liczba_punktow = 0
    for kosc in kosci:
        if kosc == pole:
            liczba_punktow += kosc
    punkty[pole-1] = liczba_punktow


def wstaw_punkty():
    pole = int(input("Gdzie chcesz wpisać punkty? (Podaj numer rubryki): "))
    if punkty[pole-1] == '':
        punkty_w_szkole(pole)
    else:
        print("Wybrane pole jest już uzupełnione")
        wstaw_punkty()



#----------------------------------------------------------------------------------------
pokaz_tabele_punktow()

for tura in range(len(kategorie)):

    print("Pierwszy rzut w turze: ")
    rzut_koscmi("12345")
    pokaz_kosci()

    for i in range(2):
        przerzut = sprawdz_czy_przerzut()
        if przerzut:
            kosci_do_przerzutu = input("Które kości chcesz przerzucić? (Podaj numery bez spacji): ")
            rzut_koscmi(kosci_do_przerzutu)
            pokaz_kosci()
        else:
            break
    
    pokaz_tabele_punktow()
    pokaz_kosci()
    wstaw_punkty()
    pokaz_tabele_punktow()

print(f"Twój łączny wynik to: {sum(punkty)}")
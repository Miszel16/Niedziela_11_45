#QUIZ
# https://quiz.giganciprogramowania.edu.pl/wdp-python2-q1

# PRZYPOMINAJKA:
# 1. Jak zbudowana jest deklaracja funkcji?


# 2. Jak działa funkcja range()?
#     - start, 
#     - stop, 
#     - step,

# 3. Pętle
#     - jakie są rodzaje? for/while
#     - jak napisać pętle?
#     - pętla nieskończona

# 4. Czym jest klasa i obiekt?
#     - jak napisać klasę/obiekt?
#     - czym jest konstruktor?
#     - czym jest dziedziczenie?





# TEKSTOWA GRA RPG
# PLAN
# - klasa bazowa: Postać (zarówno dla garacza jak i przeciwnika)
#       - konstruktor nazwa, życie, max_życie
#       - metoda atakuj (zadaje losowe obrażenia)
# - klasa pochodna: Przeciwnik (konstruktor, [goblin, szkielet, zombie])

# - klasa pochodna: Gracz (konstruktor) +
#       - metoda odpoczynek (regeneracja życia)
#       - metoda walka (przebieg walki z napotkanym przeciwnikiem)
#
# - pętla gry


from random import randint, choice

# 1. Klasa bazowa
class Postac():
    def __init__(self, nazwa, zycie):
        self.nazwa = nazwa # (gracza - podane nick) (przeciwnika - losowo)
        self.zycie = zycie
        self.max_zycie = zycie
    
    # metoda atakuj
    def atakuj(self, przeciwnik):
        atak = randint(0,3) # 0,1,2,3

        if atak == 0:
            print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}.")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadając {atak} obrażeń.")
            przeciwnik.zycie -= atak

# 2. Klasa pochodna - Przeciwnik
class Przeciwnik(Postac):
    def __init__(self, gracz):
        pula_potworow = choice(["Goblin", "Wilkołak", "Kosmita", "Olaf", "Szkielet", "Pies"])
        ogr_zycia = randint(1 , gracz.max_zycie)
        super().__init__(pula_potworow, ogr_zycia)


class Gracz(Postac):
    def __init__(self):
        nick = input("Podaj swój nick: ")
        super().__init__(nick, 10)
    
    def odpoczynek(self):
        if self.zycie < self.max_zycie:
            self.zycie += 1
        print(f"{self.nazwa} odpoczywa, aktualne życie: {self.zycie}/{self.max_zycie}.")


    def walka(self, przeciwnik):
        walka = True
        while walka:
            print()
            print(f"życie gracza: {self.zycie}")
            print(f"życie {przeciwnik.nazwa}: {przeciwnik.zycie}")
            akcja_walki = input("Akcja (atak/ucieczka): ")

            if akcja_walki == "atak":
                self.atakuj(przeciwnik)
                if przeciwnik.zycie <= 0:
                    print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                    return True
                przeciwnik.atakuj(self)
            
            elif akcja_walki == "uciekaj":
                print(f"{self.nazwa} ucieka")
                przeciwnik.atakuj(self)
                print(f"życie {self.nazwa}: {self.zycie}")
                walka = False

            else:
                print("Nieznana akcja")
            
            if self.zycie < 1:
                print(f"{self.nazwa} ginie przez {przeciwnik.nazwa}")
                return False
        return True

# pętla gry
gracz = Gracz() # konstruktor
status_gry = True
while status_gry:
    akcja = input("Akcja (zwiedzaj/odpocznij): ")
    if akcja == "zwiedzaj":
        potwor = Przeciwnik(gracz)
        print(f"{gracz.nazwa} natrafił na {potwor.nazwa}")
        gra = gracz.walka(potwor)
    elif akcja == "odpocznij":
        gracz.odpoczynek()
    else:
        print("Nieznan akcja.")
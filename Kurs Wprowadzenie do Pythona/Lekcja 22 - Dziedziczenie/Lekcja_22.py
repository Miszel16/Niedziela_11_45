# temat: DZIEDZICZENIE

# KLASA BAZOWA
class Zwierze():
    # konstruktor
    def __init__(self, wiek, imie):
        # atrybuty
        self.wiek = wiek
        self.imie = imie
        print(f"Imie zwierzaka to: {self.imie} i ma lat {self.wiek}.")
    
    # metody 
    def jedz(self):
        print(f"{self.imie} je posiłek.")
    
    def spij(self):
        print(f"{self.imie} śpi.")


zwierz1 = Zwierze(5, "Reks")
zwierz1.jedz()
zwierz1.spij()


# KLASY POCHODNE
class Pies(Zwierze):
    def __init__(self, wiek, imie, rasa):
        # uruchamia konstruktor klasy bazowej (Zwierze)
        super().__init__(wiek, imie)
        self.rasa = rasa
    
    # metody
    def wypisz_rase(self):
        print(f"{self.imie} jest rasy: {self.rasa}")

print()
pies1 = Pies(8, "Burek", "kundel")
pies1.wypisz_rase()
pies1.jedz()
pies1.spij()


# druga klasa pochodna KOT
class Kot(Zwierze):
    def __init__(self, wiek, imie, paski):
        super().__init__(wiek, imie)
        self.paski = paski
    
    def wypisz_paski(self):
        
        print(f"{self.imie} ma {self.wiek} lat oraz {self.paski} pasków.")


kot1 = Kot(8, "Figa", 50)
kot1.wypisz_paski()
kot1.jedz()
kot1.spij()


# form nazwa_pliku import nazwa_klasy
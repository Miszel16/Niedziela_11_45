class Przedmiot():
    # atrybuty
    srednia = 0

    def stworz_liste(self):
        self.oceny = []

    # metody
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def wypisz_oceny(self):
        print(f"Lista ocen: {self.oceny}")

    def oblicz_srednia(self):
        suma = sum(self.oceny)
        ilosc = len(self.oceny)
        self.srednia = suma/ilosc
        print(f"Średnia z przedmiotu: {self.srednia}")


matematyka = Przedmiot()
matematyka.stworz_liste()

matematyka.dodaj_ocene(6)
matematyka.dodaj_ocene(6)
matematyka.dodaj_ocene(6)
matematyka.dodaj_ocene(6)
matematyka.dodaj_ocene(6)

matematyka.wypisz_oceny() 

matematyka.oblicz_srednia()



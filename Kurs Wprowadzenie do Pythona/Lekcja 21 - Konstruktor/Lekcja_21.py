class Samochod():
    # ATRYBUTY - ZMIENNE
    licznik1 = 0
    # marka = ""
    # kolor = ""
    # typ = ""
    # moc_km = 0

    # METODY
    # KONSTRUKTOR 
    def __init__(self, marka: str, kolor: str, typ: str, moc_km: int):
        print("Utworzenie obiektu samochodów!")
        self.marka = marka
        self.kolor = kolor
        self.typ = typ
        self.moc_km = moc_km
        self.licznik2 = 5
        Samochod.licznik1 += 1


    def wyswietl(self):
        print(self.marka)
        print(self.kolor)
        print(self.typ)
        print(self.moc_km)
        print(f"Licznik 2: {self.licznik2}")
        print(f"Licznik1 (klasy): {Samochod.licznik1}")
        print()


# auto1 = Samochod()
# auto1.marka = "Mercedes"
# auto1.kolor = "Błękitny"
# auto1.typ = "AMG"
# auto1.moc_km = 150

auto1 = Samochod("Mercedes","Błękitny","AMG",150)
auto1.wyswietl()


auto2 = Samochod("BMW", "Czarne", "Sportowe", 200)
auto2.wyswietl()
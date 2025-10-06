# Zadanie
# Celem zadania jest stworzenie 2 klas: Kolo i Kwadrat.
# Klasy mają być odpowiedzialne za przechowywanie odpowiednich dla danej figury
# geometrycznej wymiarów oraz posiadać metody wyświetlające pole i obwod tych figur.
import math

PI = 3.1415

class Kolo():
    def __init__(self, promien):
        self.promien = promien
        self.obwod = 2 * math.pi * promien

    def pole(self):
        pole = PI * self.promien * self.promien
        print(pole)

    def wyswietl_obwod(self):
        print(f"Obwód: {self.obwod}")


kolo1 = Kolo(4)
kolo1.wyswietl_obwod()
kolo1.pole()






class Protokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b
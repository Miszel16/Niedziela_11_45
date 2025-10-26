import pygame

class Obraz():
    def __init__(self, sciezka):
        self.obraz = pygame.image.load(sciezka).convert_alpha()


# 1. Klasa bazowa
class Element():
    def __init__(self, typ):
        self.wybrany = 0
        self.lista_obrazow = []

        for i in range(1, 4): # 1 2 3
            sciezka = f"images/{typ}{i}.png" # images/body{i}.png
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz)
    
    # 0, 1, 2

    def wybierz_nastepny(self):
        self.wybrany += 1
        if self.wybrany > len(self.lista_obrazow)-1:
            self.wybrany = 0


#2. Klasy pochodne
class NakrycieGlowy(Element):
    def __init__(self):
        super().__init__("head")

# Ubranie
# Oczy
# Bron


import pygame
#     plik            klasa
from Kierunek import Kierunek

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        # image[oryginalny]    
        self.oryginalny_obraz = pygame.image.load("images/head.png")

        #surface[przerobione przez pygame]
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)

        #rect[x, y, rozmiar]
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))

        # kierunek węża
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA # może obracać się o 90 stopni
    

    def zmien_kierunek(self, kierunek):
        zmiana_mozliwa = True

        #  kierunek węża                      nasz_kierunek
        if self.kierunek == Kierunek.GORA and kierunek == Kierunek.DOL:
            zmiana_mozliwa = False

        if self.kierunek == Kierunek.PRAWO and kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False

        if self.kierunek == Kierunek.DOL and kierunek == Kierunek.GORA:
            zmiana_mozliwa = False

        if self.kierunek == Kierunek.LEWO and kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False

        if zmiana_mozliwa:
            self.nowy_kierunek = kierunek
    

    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value*-90))

        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32) # x, y

        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32, 0)

        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 32)

        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)
        
# Najlepiej sprawdzić instalację przed kazdymi zajęciami!
# # python -m pip install pygame

# Link do grafik: 
# https://drive.google.com/drive/folders/1XL7yD6J1TFTIHzx9kZtD43VT1aNHUV9G

# musimy zaimportowac plik element

import os
os.chdir(os.path.dirname(__file__))

import pygame
pygame.init()

SZEROKOSC_EKRANU = 800 
WYSOKOSC_EKRANU = 600


obraz_tla = pygame.image.load("images/background.png")# path - ścieżka
obraz_bazy_postaci = pygame.image.load("images/base.png")

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

status_gry = True
while status_gry:
    zdarzenia = pygame.event.get()

    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            status_gry = False

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(obraz_bazy_postaci, (270, 130))
    pygame.display.update()
    zegar.tick(60) 
pass   
pygame.quit()
quit()



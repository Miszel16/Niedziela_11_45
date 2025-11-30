# Gra Arkanoid - pokaz gotowego projektu
# grafiki: 
# https://drive.google.com/drive/folders/16fuwuD8Fmd3M_Uq5xATWO16AUvNRu_eM
# - prezentacja króków działania projektu

# ETAP I:
# - szablon aplikacji z tłem 
# - sterowanie platformą

import pygame
#      plik            klasa
from Platforma import Platforma

pygame.init()

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

platforma = Platforma() #!!!!!!!!!!!!!!!


status_gry = True
while status_gry:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            status_gry = False

        elif zdarzenie.type == pygame.KEYDOWN: # wykrywamy moment wciśniecia
            if zdarzenie.key == pygame.K_ESCAPE:
                status_gry = False
    
    # wykrywanie wciśnięcia
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(platforma.obraz, platforma.rect)


    pygame.display.flip() # odświeżenie
    zegar.tick(30)

pygame.quit()


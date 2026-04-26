# Gra Arkanoid - pokaz gotowego projektu
# grafiki: 
# https://drive.google.com/drive/folders/16fuwuD8Fmd3M_Uq5xATWO16AUvNRu_eM
# - prezentacja króków działania projektu

# ETAP III:
# - dodanie cegiełek do zbijania i poziomów
# - kolizja kulki z cegiełkami

import os
os.chdir(os.path.dirname(__file__))

import pygame
#      plik            klasa
from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek # !!!
pygame.init()

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

Poziom = 0 #!!!!!!!
Zycie = 3

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

# ---------------- POZIOMY ----------------
# tablica dwuwymiarowej
poziom1 = [
    [0,0,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

poziom2 = [
    [0,0,1,1,0,0,1,1,0,0],
    [0,1,2,2,1,1,2,2,1,0],
    [0,1,2,2,3,3,2,2,1,0],
    [0,0,1,1,3,3,1,1,0,0],
    [0,0,0,1,1,1,1,0,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]


klocki = pygame.sprite.Group()
def dodaj_klocki():
    wczytany_poziom = None
    if Poziom == 0:
        wczytany_poziom = poziom1
    if Poziom == 1:
        wczytany_poziom = poziom2
    
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                klocki.add(klocek)

# ------------------------------------------



platforma = Platforma()
kulka = Kulka()

status_gry = True
while status_gry:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            status_gry = False

        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                status_gry = False
    
    # wykrywanie wciśnięcia
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)
    

    # czy poziom skończony? -------------------------
    if len(klocki.sprites()) == 0:
        Poziom+=1
        if Poziom >= 2:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()   
    # -----------------------------------------------

    kulka.aktualizuj(platforma, klocki) # !!!!!!!!!!!

    if kulka.przegrana:
        Zycie -= 1
        if Zycie <= 0:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    klocki.update() #!!!!!!!!!!!!!!!!


    platforma.aktualizuj()
    ekran.blit(obraz_tla, (0,0))

    #---------------------------------------------
    for klocek in klocki:
        ekran.blit(klocek.obraz, klocek.rect)
    #---------------------------------------------

    
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)


    pygame.display.flip() # odświeżenie
    zegar.tick(30)

pygame.quit()


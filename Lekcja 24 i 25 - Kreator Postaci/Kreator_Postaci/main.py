# Najlepiej sprawdzić instalację przed kazdymi zajęciami!
# # python -m pip install pygame

# Link do grafik: 
# https://drive.google.com/drive/folders/1XL7yD6J1TFTIHzx9kZtD43VT1aNHUV9G

# musimy zaimportowac plik element

import os
os.chdir(os.path.dirname(__file__))
import Elementy
import pygame
pygame.init()

SZEROKOSC_EKRANU = 800 
WYSOKOSC_EKRANU = 600


obraz_tla = pygame.image.load("images/background.png")# path - ścieżka
obraz_bazy_postaci = pygame.image.load("images/base.png")
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

czcionka = pygame.font.SysFont('Comis Sans MS', 30)

def wypisz_tekst(ekran, tekst, pozycja):
    napis = czcionka.render(tekst, False, (255,255,255))
    # R(0-255) G(0-255) B(0-255)
    ekran.blit(napis, pozycja)

nakrycie_glowy = Elementy.NakrycieGlowy()
ubranie = Elementy.Ubrania()
oczy = Elementy.Oczy()
bron = Elementy.Bron()


status_gry = True

#--------------------
zapisywanie = False
komunikat = ""
czas_komunikatu = 0
#--------------------

while status_gry:
    zdarzenia = pygame.event.get()

    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            status_gry = False
        #Sterowanie Q - nakrycie, W - oczy, E - ubranie, R - bron
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierz_nastepny()
            if zdarzenie.key == pygame.K_w:
                oczy.wybierz_nastepny()
            if zdarzenie.key == pygame.K_e:
                ubranie.wybierz_nastepny()
            if zdarzenie.key == pygame.K_r:
                bron.wybierz_nastepny()
            # _-----------------------------
            if zdarzenie.key == pygame.K_s:
                zapisywanie = True
             # _-----------------------------  

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(obraz_bazy_postaci, (270, 130))

    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(ubranie.wybranyObraz(), (270, 130))
    ekran.blit(oczy.wybranyObraz(), (270, 130))
    ekran.blit(bron.wybranyObraz(), (270, 130))
    #------------------------------------------------------
    if zapisywanie:
        pygame.image.save(ekran, 'postac.png')
        komunikat = "Zapisano obrazek"
        czas_komunikatu = pygame.time.get_ticks() + 1000
        zapisywanie = False
    #------------------------------------------------------
    
    wypisz_tekst(ekran, f'[Q] Głowa: {nakrycie_glowy.wybrany+1}', (100, 100))
    wypisz_tekst(ekran, f'[W] Oczy: {oczy.wybrany+1}', (100, 140))
    wypisz_tekst(ekran, f'[W] Ubrania: {ubranie.wybrany+1}', (100, 180))
    wypisz_tekst(ekran, f'[W] Broń: {bron.wybrany+1}', (100, 220))
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    wypisz_tekst(ekran, f'[S] Zapisz', (100, 260))
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if pygame.time.get_ticks() < czas_komunikatu and komunikat:
        wypisz_tekst(ekran, komunikat, (300, 500))

    pygame.display.update()
    zegar.tick(60) 
pass   
pygame.quit()
quit()



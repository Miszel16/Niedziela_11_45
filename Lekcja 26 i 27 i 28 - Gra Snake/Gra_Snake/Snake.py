# GRAFIKI: https://drive.google.com/drive/folders/1qyu5_Kfb7YEJkNOJWXns0lrbWvz9Ohmw

# ETAP III:
# - zjadanie jabłka
# - nowe segmenty węża
# - wyniki na konie gry

import pygame
import random
import time
#     plik             klasa
#-------------------------------
from Kierunek import Kierunek
from Waz      import Waz
from Jablko   import Jablko
#-------------------------------
pygame.init()

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

# start, stop, step
for i in range(25): # 0-24
    for j in range(19): # 0-18 
        obraz = pygame.image.load("images/background.png")
        # R G B
        maska = (random.randrange(0, 20) ,random.randrange(0, 20), random.randrange(0, 20))
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

#----------------------------------------------------
# tworzymy węża 
waz = Waz() # konstruktor

# porusza się wąż
PORUSZ_WEZEM = pygame.USEREVENT +1 # własne zdarzenie
pygame.time.set_timer(PORUSZ_WEZEM, 200) # 200 ms
#----------------------------------------------------

jablko = Jablko() # nazwe klasy + ()
jablka_lista = pygame.sprite.Group()
jablka_lista.add(jablko)

status_gry = True 
while status_gry:
    zdarzenia = pygame.event.get()
    
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            status_gry = False
        # ---------------------------------------------------
        if zdarzenie.type == pygame.KEYDOWN:
            # a s d
            if zdarzenie.key == pygame.K_w:
                waz.zmien_kierunek(Kierunek.GORA)
            if zdarzenie.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)
            if zdarzenie.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)
            if zdarzenie.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)
        elif zdarzenie.type == PORUSZ_WEZEM:
            waz.aktualizuj()
        # ---------------------------------------------------
        pass

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka_lista)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablko = Jablko()
        jablka_lista.add(jablko)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    ekran.blit(tlo, (0,0))
    ekran.blit(waz.obraz, waz.rect)

    waz.rysuj_segmenty(ekran) #!!!!!!!!!!!!!!!!!!!


    for jablko in jablka_lista:
        ekran.blit(jablko.obraz, jablko.rect)

    pygame.display.flip()
    zegar.tick(30) # 30 FPS
pygame.quit()
quit()

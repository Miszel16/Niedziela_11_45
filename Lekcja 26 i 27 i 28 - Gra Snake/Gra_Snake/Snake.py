# GRAFIKI: https://drive.google.com/drive/folders/1qyu5_Kfb7YEJkNOJWXns0lrbWvz9Ohmw

import pygame
import random
import time
#     plik         klasa
from Jablko import Jablko
pygame.init()

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608 #!!!

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


jablko = Jablko() # nazwe klasy + ()
jablka_lista = pygame.sprite.Group()
jablka_lista.add(jablko)

status_gry = True 
while status_gry:
    zdarzenia = pygame.event.get()
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            status_gry = False
        pass

    ekran.blit(tlo, (0,0))

    for jablko in jablka_lista:
        ekran.blit(jablko.obraz, jablko.rect)

    pygame.display.flip()
    zegar.tick(30) # 30 FPS
pygame.quit()
quit()

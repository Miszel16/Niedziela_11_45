import pygame
import copy

class Klocek(pygame.sprite.Sprite):
    # konstruktor
    def __init__(self, x, y, hp_klocka):
        super(Klocek, self).__init__()
        # image surface rect
        self.obraz_oryginalny = pygame.image.load("images/brick.png")
        self.rect = pygame.Rect(x, y, 96, 48)
        self.hp_klocka = hp_klocka
    
    def aktualizuj(self):
        maska = 0
        if self.hp_klocka == 3:
            maska = (128, 0, 0)
        if self.hp_klocka == 2:
            maska = (0, 128, 0)
        if self.hp_klocka == 1:
            maska = (0, 0, 128)
        
        self.obraz = copy.copy(self.obraz_oryginalny)
        self.obraz.fill(maska, special_flags=pygame.BLEND_ADD)
    
    def update(self):
        self.aktualizuj()
    
    def uderzenie(self):
        self.hp_klocka -= 1
        if self.hp_klocka <= 0:
            self.kill()

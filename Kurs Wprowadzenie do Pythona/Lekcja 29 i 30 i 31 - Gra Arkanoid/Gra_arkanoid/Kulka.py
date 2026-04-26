import pygame
import random

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
predkosc = 15

# WEKTOR
# - kierunek (w która stronę się porusza)
# - długość (jak szybko)
# - zwrot

# "Idź w tę stronę z taką prędkością"
vec = pygame.math.Vector2 # x, y 2D

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        self.obraz = pygame.image.load("images/ball.png")
        self.r = 16
        self.zresetuj_pozycje() # zaraz napiszemy
        self.przegrana = False # czyu kulka spadła pod platforme
    

    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU-140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        self.wektor = vec(0, -predkosc) # x, y
        self.kat_nachylenia = random.randrange(-30, 30) # pod jakim kątem poleci
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False
    

    def aktualizuj(self, platforma, klocki): #!!!!!!!!!!!
        self.wspolrzedne += self.wektor # przesuniecie o 15 pikseli w danym kierunku
        self.rect.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma, klocki) #!!!!!!!!!!!
    

    def sprawdz_kolizje(self, platforma, klocki): #!!!!!!!!!!!
        # 1. krawędzie
        if self.rect.left <= 0:
            self.wektor.x *= -1 # zmiana zwrotu wektora osi x

        if self.rect.right >= SZEROKOSC_EKRANU:
            self.wektor.x *= -1 # zmiana zwrotu wektora osi x

        if self.rect.top <= 0:
            self.wektor.y *= -1 # zmiana zwrotu wektora osi y
        
        if self.rect.bottom >= WYSOKOSC_EKRANU:
            self.przegrana = True # spadamy poniżej platformy


        # 2. platforma
        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1 # zmiana zwrotu wektora osi y
            self.wektor.x += platforma.porusza_sie * 5

            if self.wektor.x < -predkosc:
                self.wektor.x = -predkosc
            if self.wektor.x > predkosc:
                self.wektor.x = predkosc
        

        # 3. klocki
        for klocek in klocki:
            # czy nastąpiła kolizja
            if self.kolizja_z_klockami(self, klocek): # stworzymy te metode po przerwie
                klocek.uderzenie()
                break


    def kolizja_z_klockami(self, kulka, klocek):
        # odległości między środkami kulki i klocka w poziomie
        dystans_x = abs(kulka.rect.centerx - klocek.rect.centerx) - klocek.rect.w/2

        dystans_y = abs(kulka.rect.centery - klocek.rect.centery) - klocek.rect.h/2

        if dystans_x < kulka.r and dystans_y < kulka.r:
            if dystans_x < dystans_y:
                self.wektor.y *= -1 # uderzenie góra/dół
            else:
                self.wektor.x *= -1 # uderzenie od boków
            return True
        return False
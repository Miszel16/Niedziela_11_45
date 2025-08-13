# ROZGRZEWKA
# Napisz funkcję, która otrzymuje 3 parametry:
# - proporcje_szerokosc
# - proporcje_wysokosc
# - piksele_szerokosc

# Funkcja otrzymuje oczekiwane proporcje ekranu (np. 16:9, 4:3) oraz piksele_szerokosc.
# Zadaniem funkcji jest obliczyć ile pikseli powinna mieć wysokość, aby proporcje ekranu
# były poprawne. Zwracana liczba powinna być liczbą całkowitą

#piksele_szerokości / proporcję_szerokości * proporcja_wysokości = piksele_wysokości

def proporcje(proporcje_szerokosc, proporcje_wysokosc, piksele_szerokosc):
    piksele_wysokosci = piksele_szerokosc / proporcje_szerokosc * proporcje_wysokosc
    return piksele_wysokosci
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PYGAME
# Pygame to specjalna biblioteka (czyli „dodatek”) do Pythona,
# która pozwala w prosty sposób tworzyć gry komputerowe i aplikacje graficzne.
# Dzięki pygame możesz:
# - wyświetlać obrazki i rysować różne kształty (np. prostokąty, koła),
# - poruszać postacią po ekranie,
# - reagować na kliknięcia myszką i naciśnięcia klawiszy,
# - odtwarzać muzykę i efekty dźwiękowe.

# Jak to działa?
# W pygame wszystko dzieje się w pętli gry, która działa cały czas:
# - Sprawdza, co zrobił gracz (np. nacisnął klawisz).
# - Aktualizuje pozycje obiektów (np. gracza).
# - Rysuje nowy obraz na ekranie.
# - Powtarza to nawet 60 razy na sekundę! 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GRAFIKI
# https://drive.google.com/file/d/1fkajJRymiESpV4i3Yut81VnuNYMIWy4c/view?usp=drive_link

import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pierwsza gra")


def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()
    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect(center = position)
    return [image, surface, rect] #oryginalny, gotowy do wyświetlenia, rozmiar i pozycje


def print_image(img_list: list):
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass


player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_path = r"C:\Users\aplac\Desktop\Projekty Python\Lekcja 12 - pygame - pierwsza aplikacja\grafiki\player.png"
player = load_image(player_path, player_pos)

clock = pygame.time.Clock()
game_status = True

while game_status:
    events = pygame.event.get()

    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            game_status = False
        pass
    
    print_image(player)

    pygame.display.update()
    clock.tick(60)
    pass

pygame.quit()
quit()

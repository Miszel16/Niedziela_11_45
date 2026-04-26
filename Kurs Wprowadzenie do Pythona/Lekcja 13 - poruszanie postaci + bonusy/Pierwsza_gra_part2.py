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


# 1. Zmiana położenia gracza na ekranie
def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center = position)
    return [image, surface, rect]

# 2. Reakcja na wciskane klawisze

def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_LSHIFT]:
        speed *= 2

    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    if keys[pygame.K_d]:
        delta_x += speed

    return [delta_x, delta_y]



player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_path = r"C:\Users\aplac\Desktop\Projekty Python\Lekcja 12 - pygame - pierwsza aplikacja\grafiki\player.png"
player = load_image(player_path, player_pos)
background_color = [9, 42, 121]

clock = pygame.time.Clock()
game_status = True
while game_status:
    events = pygame.event.get()
    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            game_status = False
        pass


    pressed_keys = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_keys)
    player_pos[0] += delta_x
    player_pos[1] += delta_y

    player = set_position_image(player, player_pos)

    screen_surface.fill(background_color)
    print_image(player)
    pygame.display.update()
    clock.tick(60)

    pass
pygame.quit()
quit()

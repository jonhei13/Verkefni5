import pygame
import sys

# SCREEN RESOLUTION
screen_x = 1280
screen_y = 720

# COLORS
green = (0, 128, 0)
yellow = (255, 255, 0)

# INITIALIZE THE GAME
pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Worms2d')


# MAKE A TEXT OBJECT
def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()


# MAKE A CLICKABLE BUTTON
def button(text, x, y, w, h, i, a):
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, a, (x, y, w, h))
        if pygame.mouse.get_pressed()[0]:
            return 1
    else:
        pygame.draw.rect(screen, i, (x, y, w, h))

    small_text = pygame.font.SysFont('arial', 20)
    text_surf, text_rect = text_objects(text, small_text)
    text_rect.center = (x+(w/2)), (y+(h/2))
    screen.blit(text_surf, text_rect)


# MENU LOOP
def game_menu():
    bg = pygame.image.load('Pics/menubg.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg, (0, 0))
        if button('Play', (screen_x*0.38), (screen_y*0.55), 120, 50, yellow, green) == 1:
            print('Start game')
            # Start game loop
        if button('Something', (screen_x*0.52), (screen_y*0.55), 120, 50, yellow, green) == 1:
            print('Something')
        pygame.display.update()



game_menu()

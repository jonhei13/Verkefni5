import pygame
import sys
from Project import LandScape

def main():
    pygame.init()
    screen_x = 1280
    screen_y = 720

    screen = pygame.display.set_mode((screen_x, screen_y))
    Terrain = LandScape.Landscape()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(Terrain.image, Terrain.rect)
        pygame.display.update()



main()

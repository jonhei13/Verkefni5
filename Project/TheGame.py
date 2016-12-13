import pygame
import sys
from Project import LandScape

pygame.init()
screen_x = 1280
screen_y = 720
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Worms2d')

done = False
def main():
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()

        screen.bl

main()

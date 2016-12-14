import pygame
from Project import spritesheet_functions
from Project import constants

from Project import Worms
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_WIDTH = constants.SCREEN_WIDTH
class Landscape(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, )
        super().__init__()
        MainImage = None
        self.worm = None
        self.rect = None

    def update(self):
        screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        #Terrain = LandScape.Landscape()
        background = pygame.Surface(screen.get_size())

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.display.update()


class LandScape01(Landscape):
    def __init__(self):
        MainImage = spritesheet_functions.SpriteSheet('Pics/Untitled.png')
        self.image = MainImage.get_image(0, 0, 1280, 720)

        self.rect = self.image.get_rect()
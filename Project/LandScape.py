import pygame
from Project import spritesheet_functions
from Project import Worms
SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720
class Landscape(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, )
        super().__init__()
        MainImage = spritesheet_functions.SpriteSheet('Pics/Untitled.png')
        self.image = MainImage.get_image(0,0,1280,720)
        self.worm = None


        self.rect = self.image.get_rect()
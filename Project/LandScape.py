import pygame
from Project import spritesheet_functions
from Project import constants
from Project import platforms

from Project import Worms
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_WIDTH = constants.SCREEN_WIDTH
class Landscape(pygame.sprite.Sprite):
    def __init__(self, worm):
        pygame.sprite.Sprite.__init__(self, )
        super().__init__()
        MainImage = None
        self.rect = None
        self.platform_list = pygame.sprite.Group()
        self.worm = worm

    def update(self):
        #screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        #Terrain = LandScape.Landscape()
        self.platform_list.update()
        #background = pygame.Surface(screen.get_size())

    def draw(self, screen):
        screen.fill(constants.BLUE)
        #screen.blit(self.image, self.rect)
        self.platform_list.draw(screen)



class LandScape01(Landscape):
    def __init__(self, worm):
        #self.image = pygame.image.load('Pics/Untitled.png').convert_alpha()
        # self.image = MainImage.get_image(0, 0, 1280, 720)
        #self.mask = pygame.mask.from_surface(self.image)
        self.platform_list = pygame.sprite.Group()
        #self.rect = self.image.get_rect()
        self.worm = worm

        level = [[platforms.BIG_ISLAND, 630, 200]]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.worm
            self.platform_list.add(block)


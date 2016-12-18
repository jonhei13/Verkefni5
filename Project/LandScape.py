import pygame
import constants
import platforms
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
        self.platform_list.update()

    def draw(self, screen):
        screen.fill(constants.BLACK)
        self.platform_list.draw(screen)



class LandScape01(Landscape):
    def __init__(self, worms):
        self.platform_list = pygame.sprite.Group()
        self.worms = worms

        level = [[platforms.BIG_ISLAND_RIGHT, 630, 720-432],
                 [platforms.BIG_ISLAND_LEFT, 0, 720-529],
                 [platforms.SMALL_ISLAND, 988, 135]]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.players = self.worms
            self.platform_list.add(block)


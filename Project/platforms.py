
import pygame

from spritesheet_functions import SpriteSheet


BIG_ISLAND_RIGHT = (630, 288, 650, 432)
BIG_ISLAND_LEFT = (0, 191, 586, 529)
SMALL_ISLAND = (988, 135, 239, 116)


class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        super().__init__()

        sprite_sheet = SpriteSheet('Pics/Untitled.png')
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

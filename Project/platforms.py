"""
Module for managing platforms.
"""
import pygame

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

BIG_ISLAND = (630, 288, 650, 432)


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

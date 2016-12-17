"""
This module is used to pull individual image from sprite aswell loads the sprite
"""
import pygame

import constants


class SpriteSheet(object):

    def __init__(self, file_name):

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):

        # Creates new blank image
        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey(constants.BLACK)

        return image
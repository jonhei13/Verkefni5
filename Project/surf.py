import pygame

from Project import spritesheet_functions as sf

SMALL_ISLAND = (988, 135, 239, 116)


class Surf(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        super().__init__()

        sprite_sheet = sf.SpriteSheet('Pics/untitled.png')

        self.image = sprite_sheet.get_image(99, 17, 238, 128)

        self.rect = self.image.get_rect()


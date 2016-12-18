import pygame

import math
import constants

from spritesheet_functions import SpriteSheet

class Aim(pygame.sprite.Sprite):
    def __init__(self, worm):
        super().__init__()

        sprite_sheet = SpriteSheet("Pics/aimer.png")

        self.image = sprite_sheet.get_image(0, 0, 636, 640)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image.set_colorkey(constants.WHITE)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.worm = worm
        self.rect.x = self.worm.rect.x - 30
        self.rect.y = self.worm.rect.y - 30
        self.direction = None
        self.changeUD = 0

    def update(self):
        self.rect.x = self.worm.rect.x
        self.rect.y = self.worm.rect.y
        if self.worm.direction == 'R':
            self.rect.y = math.cos(self.changeUD / 70) * 50 + self.worm.rect.y
            self.rect.x = -math.sin(self.changeUD / 70) * 50 + self.worm.rect.x
        else:
            self.rect.y = math.cos(self.changeUD / 70) * 50 + self.worm.rect.y
            self.rect.x = math.sin(self.changeUD / 70) * 50 + self.worm.rect.x

        # self.changeUD + self.worm.rect.y - 30

    def go_up(self):
        self.direction = 'U'
        if self.changeUD / 70 > -3 and self.changeUD / 70 < 3:
            self.changeUD -= 2

    def go_down(self):
        self.direction = 'D'
        if self.changeUD / 70 < 0:
            self.changeUD += 2

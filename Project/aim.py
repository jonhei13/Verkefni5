import pygame

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
        self.rect.x = self.worm.rect.x + 30
        self.rect.y = self.worm.rect.y + 30
        self.direction = None
        self.changeUD = 0

    def update(self):
        if self.worm.direction == 'R':
            self.rect.x = self.worm.rect.x + 30
        else:
            self.rect.x = self.worm.rect.x - 30
        self.rect.y = self.changeUD + self.worm.rect.y - 30

    def go_up(self):
        self.direction = 'U'
        self.changeUD -= 2

    def go_down(self):
        self.direction = 'D'
        self.changeUD += 2

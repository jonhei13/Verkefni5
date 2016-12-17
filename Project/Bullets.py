from spritesheet_functions import SpriteSheet
# from worm import Worm
from GunMenu import GunMenu
import pygame
import enum
import constants


class Bullet(pygame.sprite.Sprite):
    def __init__(self, worm):
        super().__init__()
        self.change_x = 0
        self.change_y = 0

        self.worm = worm

        self.level = self.worm.level

        self.name = ''
        self.movingframe_r = []
        self.movingframe_l = []

        self.image = None
        self.bulletframe_r = None
        self.bulletframe_l = None
        self.bulletframe_degreeL = None
        self.bulletframe_degreeR = None
        self.bulletframe_up = None
        self.bulletframe_down = None

        self.direction = self.worm.direction
        self.shooting = False
        self.damage = 0

        sprite_sheet = SpriteSheet('Pics/worms_sprites.png')

        # MOVING_ROCKET = sprite_sheet.get_image('1660,381,253,54')
        # HOLYBOMB = sprite_sheet.get_image()
        # GRENADE = sprite_sheet.get_image()

        if self.worm.current_gun == GunMenu.BAZOOKA:
            self.image = sprite_sheet.get_image(1891, 381, 22, 12)
            self.damage = 20
        elif self.worm.current_gun == GunMenu.GRENADE:
            self.image = sprite_sheet.get_image(1891, 381, 22, 12)
            self.damage = 30
        elif self.worm.current_gun == GunMenu.HOLYBOMB:
            self.image = sprite_sheet.get_image(1891, 381, 22, 12)
            self.damage = 45

        self.rect = self.image.get_rect()

        self.rect.x = self.worm.rect.x
        self.rect.y = self.worm.rect.y

        # Load all the right facing images
        self.bulletframe_r = self.image
        # Load all left facing images
        self.bulletframe_l = pygame.transform.flip(self.image, True, False)
        # If Rocket Load Rotated Angle to Right
        self.bulletframe_degreeR = pygame.transform.rotate(self.image, 45)
        # If Rocket Load Rotated Angle to Left
        self.bulletframe_degreeL = pygame.transform.rotate(self.image, -45)
        # Load Rocket Up
        self.bulletframe_up = pygame.transform.rotate(self.image, 45)
        # Load Rocket Down
        self.bulletframe_down = pygame.transform.rotate(self.image, 180)

    def update(self):
        self.calc_grav()
        if self.shooting:
            self.rect.y += self.change_y
            if self.direction == 'R':
                self.rect.x += self.change_x
                print('Right')
                #self.mask = pygame.mask.from_surface(self.bulletframe_r)
                self.image = self.bulletframe_r

            else:
                self.rect.x -= self.change_x
                print('Left')
                #self.mask = pygame.mask.from_surface(self.bulletframe_l)
                self.image = self.bulletframe_l
        # Check if we hit surface or player
        if self.rect.x > constants.SCREEN_WIDTH or self.rect.y > constants.SCREEN_HEIGHT or self.rect.y < 0:
            bleh = 0
            self.shooting = False

    def calc_grav(self):
        #Calculates Gravity

        self.change_y += .35

    def shoot(self):
        self.change_x = 15
        self.shooting = True
        hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False,
                                               pygame.sprite.collide_mask)
        self.change_y = (self.worm.aim.rect.y - self.worm.rect.y)/5
        if len(hit_list) > 0:
            self.change_y = self.worm.aim.rect.y

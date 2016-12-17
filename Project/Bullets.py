from spritesheet_function import SpriteSheet
from Worms import worm
from GunMenu import GunMenu
import pygame
import enum
import constants

class LoadBullets(enum.Enum):
    sprite_sheet = SpriteSheet('Pics/worms_sprites.png')
    MOVING_ROCKET = sprite_sheet.get_image('-1660,-381,253,54')
    HOLYBOMB = sprite_sheet.get_image()
    GRENADE = sprite_sheet.get_image()

class Bullets(pygame.sprite.Sprite, worm):

    def __init__(self):
        self.change_x = 0
        self.change_y = 0

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

        self.direction = 'R'
        self.shooting = False
        self.damage = 0



        if worm.current_gun == GunMenu.BAZOOKA:
            image = LoadBullets.MOVING_ROCKET
            self.damage = 20
        elif worm.current_gun == GunMenu.GRENADE:
            image = LoadBullets.GRENADE
            self.damage = 30
        elif worm.current_gun == GunMenu.HOLYBOMB:
            image = LoadBullets.HOLYBOMB
            self.damage = 45
        #Load all the right facing images
        self.bulletframe_r = pygame.transform.rotate(image, 90)
        #Load all left facing images
        self.bulletframe_l = image
        #If Rocket Load Rotated Angle to Right
        self.bulletframe_degreeR = pygame.transform.rotate(image, 45)
        #If Rocket Load Rotated Angle to Left
        self.bulletframe_degreeL = pygame.transform.rotate(image, -45)
        #Load Rocket Up
        self.bulletframe_up = pygame.transform.rotate(image, 45)
        #Load Rocket Down
        self.bulletframe_down = pygame.transform.rotate(image,180)


    def update(self):
        if self.shooting:
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            if self.direction == 'R':
               if self.shooting:
                    self.mask = pygame.mask.from_surface(self.bulletframe_r)
            else:
                if self.shooting:
                    self.mask = pygame.mask.from_surface(self.bulletframe_l)
        # Check if we hit surface or player
        if self.rect.x > constants.SCREEN_WIDTH or self.rect.y > constants.SCREEN_HEIGHT
            or self.rect.y < 0:


    def shoot(self):

        hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False,
                                               pygame.sprite.collide_mask)
        if len(hit_list) > 0:
            self.change_y += 5












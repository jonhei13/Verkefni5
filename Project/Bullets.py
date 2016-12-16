from spritesheet_function import SpriteSheet
from Worms import worm
from GunMenu import GunMenu
import pygame
import enum

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



        if worm.current_gun == GunMenu.BAZOOKA:
            image = LoadBullets.MOVING_ROCKET
        elif worm.current_gun == GunMenu.GRENADE:
            image = LoadBullets.GRENADE
        elif worm.current_gun == GunMenu.HOLYBOMB:
            image = LoadBullets.HOLYBOMB

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







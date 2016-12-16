from spritesheet_function import SpriteSheet

import pygame
from GunMenu import GunMenu

class Blullets(pygame.sprite.Sprite,GunMenu):

    def __init__(self):
        self.change_x = 0
        self.change_y = 0

        self.name = ''
        self.movingframe_r = []
        self.movingframe_l = []

        self.bulletframe_r = []
        self.bulletframe_l = []

        self.direction = 'R'

        sprite_sheet = SpriteSheet('Pics/worms_sprites.png')

        #Load all the right facing images to list


        #Load all left facing images to list


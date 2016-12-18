from spritesheet_functions import SpriteSheet
# from worm import Worm
from GunMenu import GunMenu
import pygame
import enum
import constants
import Sounds
import math

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, bullet):
        super().__init__()
        self.center = center
        self.color = constants.WHITE
        self.blast = []
        self.bullet = bullet

        green = (0, 128, 0)
        up_scale = (50, 50)


        sprite_sheet = SpriteSheet('Pics/explosion.png')
        image = sprite_sheet.get_image(10, 26, 16, 14)
        image.set_colorkey(green)
        image = pygame.transform.scale(image, up_scale)
        self.blast.append(image)
        image = sprite_sheet.get_image(37, 12, 28, 34)
        image.set_colorkey(green)
        image = pygame.transform.scale(image, up_scale)
        self.blast.append(image)
        image = sprite_sheet.get_image(81, 7, 44, 44)
        image.set_colorkey(green)
        image = pygame.transform.scale(image, up_scale)
        self.blast.append(image)
        image = sprite_sheet.get_image(136, 10, 46, 38)
        image.set_colorkey(green)
        image = pygame.transform.scale(image, up_scale)
        self.blast.append(image)
        image = sprite_sheet.get_image(189, 8, 48, 40)
        image.set_colorkey(green)
        image = pygame.transform.scale(image, up_scale)
        self.blast.append(image)

        self.image = self.blast[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.worms_already_hit = []

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame > len(self.blast)-1:
                self.kill()
            else:
                center = self.rect.center
                self.image = self.blast[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

        worm_hit_list = pygame.sprite.spritecollide(self, self.bullet.level.worms, False, pygame.sprite.collide_mask)
        for worm in worm_hit_list:
            if worm not in self.worms_already_hit:
                worm.hit_by_explosion(self)
                self.worms_already_hit.append(worm)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, active_sprite_list, worm, language):
        super().__init__()
        self.change_x = 0
        self.change_y = 0
        self.sound = Sounds.Sounds(language)
        self.active_sprite_list = active_sprite_list
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

        self.landed = None

        self.explosion = None

        sprite_sheet = SpriteSheet('Pics/worms_sprites.png')

        # MOVING_ROCKET = sprite_sheet.get_image('1660,381,253,54')
        # HOLYBOMB = sprite_sheet.get_image()
        # GRENADE = sprite_sheet.get_image()

        if self.worm.current_gun == GunMenu.BAZOOKA:
            self.image = sprite_sheet.get_image(1891, 381, 22, 12)
            self.damage = 20
        elif self.worm.current_gun == GunMenu.GRENADE:
            self.image = sprite_sheet.get_image(794, 382, 26, 24)
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.damage = 30
        elif self.worm.current_gun == GunMenu.HOLYBOMB:
            self.image = sprite_sheet.get_image(784, 331, 33, 33)
            self.image.set_colorkey(constants.WHITE)
            #self.image = pygame.transform.scale(self.image, (20, 20))
            self.damage = 45

        self.rect = self.image.get_rect()

        if self.direction == 'R':
            self.rect.x = self.worm.rect.x + 10
        else:
            self.rect.x = self.worm.rect.x - 10
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
                self.mask = pygame.mask.from_surface(self.bulletframe_r)
                self.image = self.bulletframe_r

            else:
                self.rect.x -= self.change_x
                self.mask = pygame.mask.from_surface(self.bulletframe_l)
                self.image = self.bulletframe_l


        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False, pygame.sprite.collide_mask)
        for block in block_hit_list:
            if self.rect.x > constants.SCREEN_WIDTH or self.rect.y > constants.SCREEN_HEIGHT or self.rect.y < 0:
                pass
            else:
                self.sound.get_explosion().play()
                expl = Explosion(self.rect.center, self)
                self.active_sprite_list.add(expl)
                # self.onblock = True
                self.change_x = 0
                self.change_y = 0
                self.landed = True
                self.kill()

        worm_hit_list = pygame.sprite.spritecollide(self, self.level.worms, False, pygame.sprite.collide_mask)
        for worm in worm_hit_list:
            if worm != self.worm:
                expl = Explosion(worm.rect.center, self)
                self.active_sprite_list.add(expl)
                # worm.hit(self)
                self.change_x = 0
                self.change_y = 0
                self.landed = True
                self.kill()

    def calc_grav(self):
        # Calculates Gravity

        self.change_y += .35

    def shoot(self, speed):
        y = self.worm.aim.rect.y - self.worm.rect.y
        if self.worm.direction == 'R':
            x = self.worm.aim.rect.x - self.worm.rect.x
        else:
            x = self.worm.rect.x - self.worm.aim.rect.x
        if x != 0:
            angle = math.atan(y/x)
        else:
            angle = 0
        self.change_x = speed*math.cos(angle)
        self.change_y = speed*math.sin(angle)
        self.shooting = True
        self.landed = False
        if self.worm.current_gun == GunMenu.HOLYBOMB:
            pygame.mixer.Sound('Sounds/SoundEffects/HOLYGRENADE.wav').play()
        hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False,
                                               pygame.sprite.collide_mask)
        #self.change_y = (self.worm.aim.rect.y - self.worm.rect.y)/4
        #if len(hit_list) > 0:
         #   self.change_y = self.worm.aim.rect.y

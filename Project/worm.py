"""
This module represents a single Worm instance and what he can do
"""
import pygame
import constants
import Sounds
from GunMenu import GunMenu
from spritesheet_functions import SpriteSheet


class Worm(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self, lang):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()
        # -- Attributes
        # Speed vector of the Worm
        self.change_x = 0
        self.change_y = 0

        # Player attributes
        self.life = 100
        self.name = ''
        self.team = ''
        self.current_gun = GunMenu.BAZOOKA
        self.is_dead = False
        self.is_playing = False

        self.sound = Sounds.Sounds(lang)

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        #jumping
        self.jumping_frames_r = []
        self.jumping_frames_l = []
        #Shooting
        self.shooting_frames_r = []
        self.shooting_frames_l = []
        #Grenade
        self.grenade_frames_r = []
        self.grenade_frames_l = []
        #HolyBomb
        self.holybomb_frames_r = []
        self.holybomb_frames_l = []
        #Baseball
        self.baseball_frames_r = []
        self.baseball_frames_l = []

        # What direction is the player facing?
        self.direction = "R"

        # Is player jumping?
        self.jumping = False

        #Are we on a block
        self.onblock = False

        # List of sprites we can bump against
        self.level = None

        #Our aim
        self.aim = None

        #current time left
        self.time = 30
        self.start_time = 0

        #our bullet
        self.bullet = None



        sprite_sheet = SpriteSheet("Pics/worms_sprites.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(8, 8, 22, 26)  # efst til vinstri
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(45, 8, 22, 26)  # efst í miðju
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(84, 7, 18, 27)  # efst til hægri
        self.walking_frames_l.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(8, 8, 22, 26)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(45, 8, 22, 26)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(84, 7, 18, 27)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)

        # Load players when holding a gun left
        image = sprite_sheet.get_image(191, 49, 24, 27)
        self.shooting_frames_l.append(image)

        # Load players when holding a gun right
        image = sprite_sheet.get_image(191, 49, 24, 27)
        image = pygame.transform.flip(image, True, False)
        self.shooting_frames_r.append(image)

        # Load players when holding a grenade right
        image = sprite_sheet.get_image(705, 126, 35, 40)
        image = pygame.transform.flip(image, True, False)
        self.grenade_frames_r.append(image)

        # Load players when holding a grenade left
        image = sprite_sheet.get_image(705, 126, 35, 40)
        self.grenade_frames_l.append(image)

        # Load players when holding a holy bomb right
        image = sprite_sheet.get_image(372, 126, 35, 40)
        image = pygame.transform.flip(image, True, False)
        self.holybomb_frames_r.append(image)

        # Load players when holding a holy bomb left
        image = sprite_sheet.get_image(372, 126, 35, 40)
        self.holybomb_frames_l.append(image)

        # Load players when holding a baseball bat right
        image = sprite_sheet.get_image(489, 210, 49, 47)
        image = pygame.transform.flip(image, True, False)
        self.baseball_frames_r.append(image)

        # Load players when holding a baseball bat left
        image = sprite_sheet.get_image(489, 210, 49, 47)
        self.baseball_frames_l.append(image)

        # Load player jumping left
        image = sprite_sheet.get_image(195, 5, 18, 33)  # jumping
        self.jumping_frames_l.append(image)

        # Load player jumping right
        image = sprite_sheet.get_image(195, 5, 18, 33)  # jumping
        image = pygame.transform.flip(image, True, False)
        self.jumping_frames_r.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]
        self.mask = pygame.mask.from_surface(self.image)

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Moves The Player"""
        # Gravity
        self.calc_grav()
        # Move left/right
        if self.jumping:
            self.rect.x += self.change_x
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            if self.jumping:
                    self.image = self.jumping_frames_r[0]
                    self.mask = pygame.mask.from_surface(self.image)
            else:
                if self.current_gun == GunMenu.BAZOOKA:
                    self.image = self.shooting_frames_r[0]
                    self.mask = pygame.mask.from_surface(self.image)
                elif self.current_gun == GunMenu.GRENADE:
                    self.image = self.grenade_frames_r[0]
                    self.mask = pygame.mask.from_surface(self.image)
                elif self.current_gun == GunMenu.HOLYBOMB:
                    self.image = self.holybomb_frames_r[0]
                    self.mask = pygame.mask.from_surface(self.image)
                elif self.current_gun == GunMenu.CLUB:
                    self.image = self.baseball_frames_r[0]
                    self.mask = pygame.mask.from_surface(self.image)
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            if self.jumping:
                self.image = self.jumping_frames_l[0]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                if self.current_gun == GunMenu.BAZOOKA:
                    self.image = self.shooting_frames_l[0]
                    self.mask = pygame.mask.from_surface(self.image)
                elif self.current_gun == GunMenu.GRENADE:
                    self.image = self.grenade_frames_l[0]
                    self.mask = pygame.mask.from_surface(self.image)
                elif self.current_gun == GunMenu.HOLYBOMB:
                    self.image = self.holybomb_frames_l[0]
                    self.mask = pygame.mask.from_surface(self.image)
                elif self.current_gun == GunMenu.CLUB:
                    self.image = self.baseball_frames_l[0]
                    self.mask = pygame.mask.from_surface(self.image)

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False, pygame.sprite.collide_mask)
        for block in block_hit_list:
            self.onblock = True
            self.change_x = 0
            self.jumping = False


        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False, pygame.sprite.collide_mask)
        for block in block_hit_list:
            self.onblock = True
            #Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.change_y = 0
            elif self.change_y < 0:
                self.change_y = 0

            # Stop our vertical movement
            self.change_y = 0
            self.jumping = False

    def calc_grav(self):
        #Calculates Gravity
        if not self.onblock:
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .35
        if self.rect.y <= 0:
            self.change_y = 1
            self.onblock = False
    def jump(self):
        # Worm Jumps
        self.onblock = False
        self.jumping = True
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False,
                                                        pygame.sprite.collide_mask)
        self.rect.y -= 2
        self.sound.get_jump().play()

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -5

    def hit(self, bullet):
        self.onblock = False
        self.jumping = True
        if bullet.direction == 'R':
            self.change_x = bullet.damage*0.3
        else:
            self.change_x = -bullet.damage
        self.change_y = -bullet.damage*0.1
        self.life -= bullet.damage
        self.sound.get_ouch().play()
        self.update()

    def hit_by_explosion(self, explosion):
        self.onblock = False
        self.jumping = True
        if self.rect.x > explosion.rect.x:
            self.change_x = explosion.bullet.damage
        else:
            self.change_x = -explosion.bullet.damage
        self.change_y = -explosion.bullet.damage*0.3
        self.life -= explosion.bullet.damage
        self.sound.get_ouch().play()
        self.sound.get_explosion().play()
        self.update()

    # Player-controlled movement:
    def go_left(self):
        #Checks if player is inside the scope and moves when user hits jump and left arrow
        self.direction = "L"
        if self.jumping:
            if self.rect.x-10 < 0:
                self.change_x = 0
            else:
                self.change_x = -3

            self.onblock = False

    def go_right(self):
        # Checks if player is inside the scope and moves when user hits jump and right arrow
        self.direction = "R"
        if self.jumping:
            if self.rect.x+15 >= constants.SCREEN_WIDTH:
                self.change_x = 0
            else:
                self.change_x = 3
            self.onblock = False


    def stop(self):
        #When no buttons are pressed
        self.change_x = 0
        self.onblock = False


"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

from spritesheet_functions import SpriteSheet


class Worm(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        # jumping
        self.jumping_frames_r = []
        self.jumping_frames_l = []

        self.shooting_frames_r = []
        self.shooting_frames_l = []

        # What direction is the player facing?
        self.direction = "R"

        # Is player jumping?
        self.jumping = False

        #Are we on a block
        self.onblock = False

        # List of sprites we can bump against
        self.level = None

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

        #Load players when holding a gun left
        image = sprite_sheet.get_image(191, 49, 24, 27)
        self.shooting_frames_l.append(image)

        # Load players when holding a gun right
        image = sprite_sheet.get_image(191, 49, 24, 27)
        image = pygame.transform.flip(image, True, False)
        self.shooting_frames_r.append(image)

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
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        if(self.jumping):
            self.rect.x += self.change_x
        pos = self.rect.x #+ self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            if self.jumping:
                self.image = self.jumping_frames_r[0]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.shooting_frames_r[0]
                self.mask = pygame.mask.from_surface(self.image)
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            if self.jumping:
                self.image = self.jumping_frames_l[0]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.shooting_frames_l[0]
                self.mask = pygame.mask.from_surface(self.image)

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False, pygame.sprite.collide_mask)
        for block in block_hit_list:
            self.onblock = True
            # If we are moving right,
            # set our right side to the left side of the item we hit
            #self.change_x = 0
            self.change_x = 0
            if self.change_x > 0:
                self.change_x = 0
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.change_x = 0

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False, pygame.sprite.collide_mask)
        for blokc in block_hit_list:
            #self.change_y = 0
            self.onblock = True
            #Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.change_y = 0
            elif self.change_y < 0:
                self.change_y = 0

            # Stop our vertical movement
            self.change_y = 0
            self.jumping = False

            #if isinstance(block, MovingPlatform):
             #   self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if not self.onblock:
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .35

        # See if we are on the ground.
        # if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
        #     self.change_y = 0
        #     self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
        #     self.jumping = False

    def jump(self):
        """ Called when user hits 'jump' button. """
        self.onblock = False
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False,
                                                        pygame.sprite.collide_mask)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -5
            #self.jumping = True

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.direction = "L"
        if self.jumping:
            self.change_x = -3

            self.onblock = False

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.direction = "R"
        if self.jumping:
            self.change_x = 3

            self.onblock = False

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.onblock = False

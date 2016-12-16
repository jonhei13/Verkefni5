import pygame
import enum


class GunMenu(enum.Enum):
        BAZOOKA = pygame.transform.scale(pygame.image.load('Pics/GunMenu/FirstChosen.png'), (210, 50))
        GRENADE = pygame.transform.scale(pygame.image.load('Pics/GunMenu/SecondChosen.png'), (210, 50))
        HOLYBOMB = pygame.transform.scale(pygame.image.load('Pics/GunMenu/ThirdChosen.png'), (210, 50))
        CLUB = pygame.transform.scale(pygame.image.load('Pics/GunMenu/FourthChosen.png'), (210, 50))



        # self.img_list = list()
        #
        # self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/FirstChosen.png'), (210, 50)))
        # self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/SecondChosen.png'), (210, 50)))
        # self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/ThirdChosen.png'), (210, 50)))
        # self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/FourthChosen.png'), (210, 50)))

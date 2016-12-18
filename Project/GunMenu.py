import pygame
import enum


class GunMenu(enum.Enum):
        BAZOOKA = pygame.transform.scale(pygame.image.load('Pics/GunMenu/FirstChosen.png'), (160, 50))
        GRENADE = pygame.transform.scale(pygame.image.load('Pics/GunMenu/SecondChosen.png'), (160, 50))
        HOLYBOMB = pygame.transform.scale(pygame.image.load('Pics/GunMenu/ThirdChosen.png'), (160, 50))


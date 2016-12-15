import pygame


class GunMenu:
    def __init__(self):
        self.chosen = 1

    def choose_gun(self, get_image):
        self.img_list = []
        self.chosen = get_image

        self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/FirstChosen.png'), (210, 50)))
        self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/SecondChosen.png'), (210, 50)))
        self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/ThirdChosen.png'), (210, 50)))
        self.img_list.append(pygame.transform.scale(pygame.image.load('Pics/GunMenu/FourthChosen.png'), (210, 50)))
        return self.img_list[get_image]







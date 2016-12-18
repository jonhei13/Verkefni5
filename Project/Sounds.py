import pygame
import random


class Sounds:
    ouch = []
    jump = []

    def __init__(self, language):
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OUCH.wav'))
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OW1.wav'))
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OW2.wav'))
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OW3.wav'))

        self.jump.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/JUMP1.wav'))
        self.jump.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/JUMP2.wav'))

    def get_ouch(self):
        return self.ouch[random.randint(0, 4)]

    def get_jump(self):
        return self.jump[random.randint(0, 2)]

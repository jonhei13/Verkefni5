import pygame
import random


class Sounds:
    ouch = []
    jump = []
    explosion = []

    def __init__(self, language):
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OUCH.wav'))
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OW1.wav'))
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OW2.wav'))
        self.ouch.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/OW3.wav'))

        self.jump.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/JUMP1.wav'))
        self.jump.append(pygame.mixer.Sound('Sounds/Languages/' + language + '/JUMP2.wav'))

        self.explosion.append(pygame.mixer.Sound('Sounds/SoundEffects/Explosion1.wav'))
        self.explosion.append(pygame.mixer.Sound('Sounds/SoundEffects/Explosion2.wav'))
        self.explosion.append(pygame.mixer.Sound('Sounds/SoundEffects/Explosion3.wav'))
    def get_ouch(self):
        return self.ouch[random.randint(0, 3)]

    def get_jump(self):
        return self.jump[random.randint(0, 1)]

    def get_explosion(self):
        return self.explosion[random.randint(0, 2)]

import pygame

class Landscape(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.moveY = 0
        self.moveX = 0
        self.image.fill('0,0,255')
        self.image = pygame.Surface([width, height])
        self.player = None
        self.rect = self.image.get.rect()


    def update(self):
        #See if we hit the player
        hit = pygame.sprite.collide_rect(self,self.player)

        #Movement Up And Down
        self.rect.y += self.moveY
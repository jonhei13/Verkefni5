import pygame

SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720
class Landscape(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.image.load('Pics/Untitled.png').convert()
        self.rect = self.image.get_rect()



    # def GetImage(self):
    #
    #     image = pygame.Surface([])
    #     image.blit(self,(0,0), ())
    #     image.set_colorkey('0,0,255')
    #     return image
    #
    # def update(self):
    #     #See if we hit the player
    #     hit = pygame.sprite.collide_rect(self,self.player)
    #
    #     #Movement Up And Down
    #     self.rect.y += self.moveY
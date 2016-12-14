from cmath import rect

import pygame
import sys
from Project import LandScape
from Project import worm
from Project import constants

def main():
    pygame.init()
    screen_x = constants.SCREEN_WIDTH
    screen_y = constants.SCREEN_HEIGHT

    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Ormstunga")

    player = worm.Worm()

    current_level = LandScape.LandScape01(player)

    #background = pygame.Surface(screen.get_size())

    active_sprite_list = pygame.sprite.Group()


    player.rect.x = 150
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    player.level = current_level

    active_sprite_list.add(player)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_UP:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()

        active_sprite_list.update()

        current_level.update()

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()

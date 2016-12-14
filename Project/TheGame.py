from cmath import rect

import pygame
import sys
from Project import LandScape
from Project import worm
from Project import constants

def main():
    pygame.init()
    screen_x = 1280
    screen_y = 720

    screen = pygame.display.set_mode((screen_x, screen_y))
    level = LandScape.LandScape01()
    background = pygame.Surface(screen.get_size())
    active_sprite_list = pygame.sprite.Group()

    player = worm.Worm()
    player.rect.x = 150
    player.rect.y = 150
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

        level.draw(screen)
        active_sprite_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

main()

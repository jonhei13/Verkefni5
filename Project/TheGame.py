from cmath import rect

import pygame
import sys
from Project import LandScape
from Project import worm
from Project import constants
from Project import GunMenu


def main():
    pygame.init()
    screen_x = constants.SCREEN_WIDTH
    screen_y = constants.SCREEN_HEIGHT

    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Ormstunga")

    player = worm.Worm()

    current_level = LandScape.LandScape01(player)

    # Starting weapon of choice
    g_menu = GunMenu.GunMenu()
    img = g_menu.choose_gun(0)
    #background = pygame.Surface(screen.get_size())

    active_sprite_list = pygame.sprite.Group()

    player.rect.x = 950
    player.rect.y = 50 - player.rect.height
    player.level = current_level

    active_sprite_list.add(player)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        active_sprite_list.update()
        current_level.update()
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_SPACE:
                player.jumping = True
                player.jump()
            if event.key == pygame.K_1:
                img = g_menu.choose_gun(0)
            if event.key == pygame.K_2:
                img = g_menu.choose_gun(1)
            if event.key == pygame.K_3:
                img = g_menu.choose_gun(2)
            if event.key == pygame.K_4:
                img = g_menu.choose_gun(3)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
        print(g_menu.chosen)
        screen.blit(img, (constants.SCREEN_WIDTH-img.get_width(), constants.SCREEN_HEIGHT-img.get_height()))

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()

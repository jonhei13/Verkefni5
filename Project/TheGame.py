from cmath import rect

import pygame
import sys
import random
from time import sleep
import LandScape
import worm
import constants
import GunMenu
import aim
import GameMenu
import Team


#####
#player turn time
turntime = 20



def main(team_blue, team_red):
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 25)

    screen_x = constants.SCREEN_WIDTH
    screen_y = constants.SCREEN_HEIGHT

    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Ormstunga")

    # Starting weapon of choice
    g_menu = GunMenu.GunMenu
    img = g_menu.BAZOOKA

    player_list = []

    red_team = Team.Team(team_red)
    blue_team = Team.Team(team_blue)

    for p in team_blue:
        player = worm.Worm()
        player.team = 'BLUE'
        player.name = p
        player_list.insert(random.randint(0, len(team_blue)), player)

    for p in team_red:
        player = worm.Worm()
        player.team = 'RED'
        player.name = p
        player_list.insert(random.randint(0, len(team_red)), player)

    active_sprite_list = pygame.sprite.Group()
    #background = pygame.Surface(screen.get_size())
    for man in player_list:
        current_level = LandScape.LandScape01(man)
        man.rect.x = random.randint(700, 950)
        man.rect.y = 50 - man.rect.height
        man.level = current_level
        man.aim = aim.Aim(man)
        active_sprite_list.add(man)
        active_sprite_list.add(man.aim)

    clock = pygame.time.Clock()
    player = player_list.pop()
    player.start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        active_sprite_list.update()
        current_level.update()
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        #print players time
        label = myfont.render(str(int(player.time)), 2, (255, 0, 0))
        screen.blit(label, (player.rect.x+5, player.rect.y - 20))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_SPACE:
                player.jumping = True
                player.jump()
            if event.key == pygame.K_UP:
                player.aim.go_up()
            if event.key == pygame.K_DOWN:
                player.aim.go_down()
            if event.key == pygame.K_1:
                img = g_menu.BAZOOKA
                player.current_gun = g_menu.BAZOOKA
            if event.key == pygame.K_2:
                img = g_menu.GRENADE
                player.current_gun = g_menu.GRENADE
            if event.key == pygame.K_3:
                img = g_menu.HOLYBOMB
                player.current_gun = g_menu.HOLYBOMB
            if event.key == pygame.K_4:
                img = g_menu.CLUB
                player.current_gun = g_menu.CLUB
            if event.key == pygame.K_KP0:
                sleep(0.2)
                player_list.insert(0, player)
                player = player_list.pop()
                print('BOOM - It is: ', player.name + "'s"', Turn')
                player.start_time = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
        print(player.time)
        #Stop if player time is over
        player.time = turntime - (pygame.time.get_ticks() - player.start_time) / 1000
        if player.time <= 0:
            player_list.insert(0, player)
            player = player_list.pop()
            print('BOOM - It is: ', player.name + "'s"', Turn')
            player.start_time = pygame.time.get_ticks()

        if int(player.rect.y) > screen_y:
            pass  # TODO: Remove dead players from screen and where they don't belong

        screen.blit(img.value, (screen_x-img.value.get_width(), screen_y-img.value.get_height()))

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    GameMenu.game_menu()

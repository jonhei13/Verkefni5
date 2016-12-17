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

    health_font = pygame.font.SysFont("monospace", 22)
    team_health_font = pygame.font.SysFont("monospace", 22, bold=True)
    time_font = pygame.font.SysFont("monospace", 30, bold=True)

    screen_x = constants.SCREEN_WIDTH
    screen_y = constants.SCREEN_HEIGHT

    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Ormstunga")

    # Starting weapon of choice
    g_menu = GunMenu.GunMenu
    img = g_menu.BAZOOKA

    player_list = []

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

    red_team = Team.Team([x for x in player_list if x.team == 'RED'])
    blue_team = Team.Team([x for x in player_list if x.team == 'BLUE'])

    red_team_logo = pygame.transform.scale(pygame.image.load('Pics/Menu/team_red_logo.png'), (100, 24))
    blue_team_logo = pygame.transform.scale(pygame.image.load('Pics/Menu/team_blue_logo.png'), (100, 24))

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
    counter = 0
    player = player_list[counter]
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

        blue_team.update([x for x in player_list if x.team == 'BLUE' and x.is_dead is False])
        red_team.update([x for x in player_list if x.team == 'RED' and x.is_dead is False])

        time = time_font.render(str(int(player.time)), 2, (255, 255, 0))
        screen.blit(time, (20, 680))

        red_team_health = team_health_font.render(str(red_team.team_health), 2, (255, 0, 0))
        blue_team_health = team_health_font.render(str(blue_team.team_health), 2, (255, 0, 0))

        screen.blit(red_team_health, ((screen_x/2)-30, 30))
        screen.blit(blue_team_health, ((screen_x / 2) + 30, 30))

        screen.blit(red_team_logo, ((screen_x/2)-140, 30))
        screen.blit(blue_team_logo, ((screen_x/2) + 78, 30))

        for players in player_list:
            health = health_font.render(str(players.life), 2, (255, 0, 0))
            screen.blit(health, (players.rect.x, players.rect.y - 20))

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
                if counter == len(player_list)-1:
                    counter = -1
                counter += 1
                sleep(0.2)
                player = player_list[counter]
                print('BOOM - It is: ', player.name + "'s"', Turn')
                player.start_time = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()

        #Stop if player time is over
        player.time = turntime - (pygame.time.get_ticks() - player.start_time) / 1000
        if player.time <= 0:
            if counter == len(player_list)-1:
                counter = -1
            counter += 1
            player = player_list[counter]
            print('BOOM - It is: ', player.name + "'s"', Turn')
            player.start_time = pygame.time.get_ticks()

        if int(player.rect.y) > screen_y:
            player.is_dead = True
            pass  # TODO: Remove dead players from screen and where they don't belong

        screen.blit(img.value, (screen_x-img.value.get_width(), screen_y-img.value.get_height()))

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main(['Gunni', 'Arnar'], ['Siggi', 'Jonni'])

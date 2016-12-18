from cmath import rect

import pygame
import sys
import random
import LandScape
import worm
import constants
import GunMenu
import aim
import GameMenu
import Team
import Bullets
import itertools

#####
#player turn time
turntime = 20


def get_player(cycle_r, cycle_b, last_team):
    try:
        if last_team:
            return cycle_r.__next__()
        return cycle_b.__next__()
    except StopIteration:
        pass


def main(team_blue, team_red, language):
    pygame.init()
    pygame.mixer.init()

    health_font = pygame.font.SysFont("monospace", 12)
    name_font = pygame.font.SysFont("monospace", 12)
    team_health_font = pygame.font.SysFont("monospace", 22, bold=True)
    time_font = pygame.font.SysFont("monospace", 30, bold=True)

    screen_x = constants.SCREEN_WIDTH
    screen_y = constants.SCREEN_HEIGHT
    speed = 0
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Ormstunga")
    won = False
    RedWin = False
    BlueWin = False
    # Starting weapon of choice
    g_menu = GunMenu.GunMenu
    img = g_menu.BAZOOKA

    player_list = []

    for p in team_blue:
        player = worm.Worm(language)
        player.team = 'BLUE'
        player.name = p
        player_list.insert(random.randint(0, len(team_blue)), player)

    for p in team_red:
        player = worm.Worm(language)
        player.team = 'RED'
        player.name = p
        player_list.insert(random.randint(0, len(team_red)), player)
    red_team = Team.Team([x for x in player_list if x.team == 'RED'])
    blue_team = Team.Team([x for x in player_list if x.team == 'BLUE'])

    red_team_logo = pygame.transform.scale(pygame.image.load('Pics/Menu/team_red_logo.png'), (100, 24))
    blue_team_logo = pygame.transform.scale(pygame.image.load('Pics/Menu/team_blue_logo.png'), (100, 24))
    red_team_wins = pygame.transform.scale(pygame.image.load('Pics/rtw.png'), (500, 200))
    blue_team_wins = pygame.transform.scale(pygame.image.load('Pics/btw.png'), (500, 200))
    play_again = pygame.transform.scale(pygame.image.load('Pics/play_again.png'), (155, 47))

    active_sprite_list = pygame.sprite.Group()
    #background = pygame.Surface(screen.get_size())
    current_level = LandScape.LandScape01(player_list)
    for man in player_list:
        if man.team == 'BLUE':
            man.rect.x = random.randint(1100, 1200)
        else:
            man.rect.x = random.randint(250, 400)
        man.rect.y = 50 - man.rect.height
        man.level = current_level
        man.aim = aim.Aim(man)
        active_sprite_list.add(man)
        active_sprite_list.add(man.aim)

    clock = pygame.time.Clock()

    team_played = True

    red_team_cycle = itertools.cycle(red_team.members)
    blue_team_cycle = itertools.cycle(blue_team.members)

    player = get_player(red_team_cycle, blue_team_cycle, team_played)
    player.is_playing = True
    player.start_time = pygame.time.get_ticks()
    team_played = not team_played
    PlayerDel = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        for RedWorm in red_team.members:
            if RedWorm.life <= 0 and player_list != []:
                player_list.remove(RedWorm)
                RedWorm.kill()
                RedWorm.aim.kill()
                PlayerDel = True

        for BlueWorm in blue_team.members:
            if BlueWorm.life <= 0 and player_list != []:
                player_list.remove(BlueWorm)
                BlueWorm.kill()
                BlueWorm.aim.kill()
                PlayerDel = True


        if PlayerDel:
            pl_team = player.team
            if pl_team == 'BLUE':
                blue_team.update([x for x in player_list if x.team == 'BLUE'])
                blue_team_cycle = itertools.cycle(blue_team.members)
                team_played = True
            else:
                red_team.update([x for x in player_list if x.team == 'RED'])
                red_team_cycle = itertools.cycle(red_team.members)
                team_played = False
            player = get_player(red_team_cycle, blue_team_cycle, team_played)
            player.is_playing = True
            team_played = not team_played
            player.start_time = pygame.time.get_ticks()
            PlayerDel = False

        active_sprite_list.update()
        current_level.update()
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        time = time_font.render(str(int(player.time)), 2, (255, 255, 0))
        screen.blit(time, (20, 680))

        red_team_health = team_health_font.render(str(red_team.team_health), 2, (255, 255, 255))
        blue_team_health = team_health_font.render(str(blue_team.team_health), 2, (255, 255, 255))

        screen.blit(red_team_health, ((screen_x/2)-30, 30))
        screen.blit(blue_team_health, ((screen_x / 2) + 30, 30))

        screen.blit(red_team_logo, ((screen_x/2)-140, 30))
        screen.blit(blue_team_logo, ((screen_x/2) + 78, 30))

        for players in player_list:
            if players.is_playing:
                pn = name_font.render(str(players.name), 2, (255, 255, 255))
                screen.blit(pn, (players.rect.x, players.rect.y - 40))
            else:
                if players.team == 'BLUE':
                    pn = name_font.render(str(players.name), 2, (0, 0, 255))
                    screen.blit(pn, (players.rect.x, players.rect.y - 40))
                else:
                    pn = name_font.render(str(players.name), 2, (255, 0, 0))
                    screen.blit(pn, (players.rect.x, players.rect.y - 40))

            health = health_font.render(str(players.life), 2, (255, 255, 255))
            screen.blit(health, (players.rect.x, players.rect.y - 20))
        if not won:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_SPACE:
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
                # shoot on keypad 0 down
                if event.key == pygame.K_KP0:
                    red_team.update([x for x in player_list if x.team == 'RED'])
                    blue_team.update([x for x in player_list if x.team == 'BLUE'])
                    b = False
                    if len(red_team.members) > 0 and len(blue_team.members) > 0:
                        keys = pygame.key.get_pressed()
                        f = True
                        while keys[pygame.K_KP0] and f:
                            speed += 0.00005
                            for e in pygame.event.get():
                                if e.type == pygame.KEYUP:
                                    player.bullet = Bullets.Bullet(active_sprite_list, player, language)
                                    player.bullet.shoot(speed)
                                    active_sprite_list.add(player.bullet)
                                    player.is_playing = False
                                    player = get_player(red_team_cycle, blue_team_cycle, team_played)
                                    player.is_playing = True
                                    team_played = not team_played
                                    player.start_time = pygame.time.get_ticks()
                                    f = False
                                    speed = 0
                                    break
                    else:
                        if len(blue_team.members) == 0:
                            won = True
                            RedWin = True
                        if len(red_team.members) == 0:
                            won = True
                            BlueWin = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()


            # Stop if player time is over
            player.time = turntime - (pygame.time.get_ticks() - player.start_time) / 1000
            if player.time <= 0:
                player.is_playing = False
                player = get_player(red_team_cycle, blue_team_cycle, team_played)
                team_played = not team_played
                player.is_playing = True
                player.start_time = pygame.time.get_ticks()

            # Dying
            if int(player.rect.y) > screen_y and player_list != []:
                player_list.remove(player)
                player.kill
                player.aim.kill
                pl_team = player.team
                if not won:
                    if pl_team == 'BLUE':
                        blue_team.update([x for x in player_list if x.team == 'BLUE'])
                        blue_team_cycle = itertools.cycle(blue_team.members)
                        team_played = True
                    else:
                        red_team.update([x for x in player_list if x.team == 'RED'])
                        red_team_cycle = itertools.cycle(red_team.members)
                        team_played = False
                    player = get_player(red_team_cycle, blue_team_cycle, team_played)
                    player.is_playing = True
                    team_played = not team_played
                    player.start_time = pygame.time.get_ticks()

            if len(blue_team.members) == 0:
                won = True
                RedWin = True
            if len(red_team.members) == 0:
                won = True
                BlueWin = True

        mouse = pygame.mouse.get_pos()

        if RedWin:
            screen.blit(red_team_wins, ((screen_x / 2) - 250, 200))
            screen.blit(play_again, ((screen_x / 2) - 77.5, 400))
            if (screen_x / 2) - 77.5 < mouse[0] < (screen_x / 2) + 77.5 and 400 < mouse[1] < 447:
                if pygame.mouse.get_pressed()[0]:
                    GameMenu.game_menu()
        elif BlueWin:
            screen.blit(blue_team_wins, ((screen_x / 2) - 250, 200))
            screen.blit(play_again, ((screen_x / 2) - 77.5, 400))
            if (screen_x / 2) - 77.5 < mouse[0] < (screen_x / 2) + 77.5 and 400 < mouse[1] < 447:
                if pygame.mouse.get_pressed()[0]:
                    GameMenu.game_menu()

        screen.blit(img.value, (screen_x-img.value.get_width(), screen_y-img.value.get_height()))

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    GameMenu.game_menu()


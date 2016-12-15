import pygame
import sys
from Project import constants as c
from time import sleep

# Initializers
pygame.init()
pygame.mixer.init()
pygame.font.init()
menu_song = pygame.mixer.Sound('Sounds/menu_song.wav')
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pygame.display.set_caption('Ormar')
txt = pygame.font.Font('freesansbold.ttf', 15)
clock = pygame.time.Clock()


# Get input to input box
def input_box(team_list, team_input_box, inpb_x, inpb_y):
    name = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and len(name) < 10:
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_SPACE:
                    name += ' '
                elif event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_RETURN:
                    screen.blit(team_input_box, (inpb_x, inpb_y))
                    pygame.display.update()
                    if len(name) <= 0:
                        print('name too short')
                    elif name in team_list:
                        print('name already taken')
                    elif name not in team_list:
                        team_list.append(name)
                        return
            elif event.type == pygame.QUIT:
                return
        screen.blit(team_input_box, (inpb_x, inpb_y))
        the_text = txt.render(name, True, c.WHITE)
        screen.blit(the_text, (inpb_x + 15, inpb_y + 10))
        pygame.display.update()


# Return a loaded and resized image
def im_resize(img_path, r_x, r_y):
    return pygame.transform.scale(pygame.image.load(img_path), (r_x, r_y))


# Check for click and show image
def button(pic, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if pygame.mouse.get_pressed()[0]:
            return True

    screen.blit(pic, (x, y))


# Remove player from team
def remove_player(mouse, team_list):
    try:
        if 190 > mouse[1] > 170:
            team_list.pop(0)
        elif 210 > mouse[1] > 190:
            team_list.pop(1)
        elif 230 > mouse[1] > 210:
            team_list.pop(2)
        elif 250 > mouse[1] > 230:
            team_list.pop(3)
        elif 270 > mouse[1] > 250:
            team_list.pop(4)
        elif 290 > mouse[1] > 270:
            team_list.pop(5)
        elif 310 > mouse[1] > 290:
            team_list.pop(6)
        elif 330 > mouse[1] > 310:
            team_list.pop(7)
    except IndexError:
        pass


# MENU LOOP
def game_menu():
    menu_song.play(-1)
    red_list = []
    blue_list = []
    blue_column = 175
    red_column = 175
    rem = txt.render('Del', True, c.BLACK)
    add = txt.render('Add player', True, c.WHITE)

    bg = pygame.image.load('Pics/Menu/menubg.png')
    title = im_resize('Pics/Menu/game_title.png', 314, 169)
    pb = im_resize('Pics/Menu/play.png', 90, 50)
    pb_p = im_resize('Pics/Menu/play_pressed.png', 90, 50)
    tb = im_resize('Pics/Menu/team_blue.png', 200, 300)
    tr = im_resize('Pics/Menu/team_red.png', 200, 300)
    tb_logo = im_resize('Pics/Menu/team_blue_logo.png', 200, 50)
    tr_logo = im_resize('Pics/Menu/team_red_logo.png', 200, 50)
    r_inp = im_resize('Pics/Menu/red_input.png', 166, 30)
    b_inp = im_resize('Pics/Menu/blue_input.png', 165, 30)
    r_inp_p = im_resize('Pics/Menu/red_input_pressed.png', 166, 30)
    b_inp_p = im_resize('Pics/Menu/blue_input_pressed.png', 165, 30)

    while True:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display background and title
        screen.blit(bg, (0, 0))
        screen.blit(title, (485, 20))

        # Display blue and red logo
        screen.blit(tb_logo, (130, 90))
        screen.blit(tr_logo, (950, 90))

        # Display blue and red columns
        screen.blit(tb, (130, 150))
        screen.blit(tr, (950, 150))

        # Display team members in column
        for name in blue_list:
            the_text = txt.render(name, True, c.WHITE)
            screen.blit(the_text, (155, blue_column))
            screen.blit(rem, (275, blue_column))
            blue_column += 20
        blue_column = 175

        for name in red_list:
            the_text = txt.render(name, True, c.WHITE)
            screen.blit(the_text, (972, red_column))
            screen.blit(rem, (1092, red_column))
            red_column += 20
        red_column = 175

        # Play button
        if button(pb, 600, 300, 90, 50):
            screen.blit(pb_p, (600, 304))
            if len(blue_list) > 1 and len(red_list) > 1:
                return blue_list, red_list

        # Removing player from team
        if 300 > mouse[0] > 130:
            if 450 > mouse[1] > 150:
                if pygame.mouse.get_pressed()[0]:
                    remove_player(mouse, blue_list)
                    sleep(0.2)
        if 1120 > mouse[0] > 950:
            if 450 > mouse[1] > 150:
                if pygame.mouse.get_pressed()[0]:
                    remove_player(mouse, red_list)
                    sleep(0.2)

        screen.blit(add, (970, 132))

        # Blue and red input boxes
        if button(r_inp, 963, 132, 155, 35) and len(red_list) < 8:
            screen.blit(b_inp, (145, 132))
            screen.blit(r_inp_p, (963, 132))
            screen.blit(add, (155, 139))
            input_box(red_list, r_inp_p, 963, 132)

        if button(b_inp, 145, 132, 155, 35) and len(blue_list) < 8:
            screen.blit(b_inp_p, (145, 132))
            screen.blit(r_inp, (963, 132))
            screen.blit(add, (973, 139))
            input_box(blue_list, b_inp_p, 145, 132)

        # Display add text in input boxes
        screen.blit(add, (155, 139))
        screen.blit(add, (973, 139))
        pygame.display.update()

game_menu()

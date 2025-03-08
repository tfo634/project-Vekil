import pygame
import random
from time import time

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1700, 960))
pygame.display.set_caption('Game')
background = pygame.image.load('bg.png').convert()
move_right = [
    pygame.image.load('player_fd2.png').convert_alpha(),
    pygame.image.load('player_fd1.png').convert_alpha(),
    pygame.image.load('player_fd3.png').convert_alpha(),
    pygame.image.load('player_fd2.png').convert_alpha()
]
move_left = [
    pygame.image.load('player_fd2.1.png').convert_alpha(),
    pygame.image.load('player_fd1.1.png').convert_alpha(),
    pygame.image.load('player_fd3.1.png').convert_alpha(),
    pygame.image.load('player_fd2.1.png').convert_alpha()
]

time_now = time()

txt = pygame.font.Font('Oswald-Light.ttf', 100)
text_ls = txt.render('YOU LOSE', False, 'Red')
text_ta = txt.render('Try Again', False, 'Green')
text_ta_hb = text_ta.get_rect(topleft=(700, 400))
cnt = pygame.font.Font('Oswald-Light.ttf', 50)

lst = [700, 600, 700, 700]

animation = 0
background_x = 0

player_speed = 15
player_x = 400
player_y = 720

enemy = pygame.image.load('enemy1.png').convert_alpha()
enemy_x = 1000
enemy_list = []
enemy_tick = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_tick, 700)

game = True

jump = False
jump_height = 20

running = True
while running:
    sek = cnt.render(str(int(time() - time_now)), False, 'Black')
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 1700, 0))
    if game:
        screen.blit(sek, (1650, 50))
        player_hb = move_left[0].get_rect(topleft=(player_x, player_y))
        if enemy_list:
            for (num, element) in enumerate(enemy_list):
                screen.blit(enemy, element)
                element.x -= 20
                if element.x < -100:
                    enemy_list.pop(num)
                if player_hb.colliderect(element):
                    speed = 400
                    game = False
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            screen.blit(move_left[animation], (player_x, player_y))
        else:
            screen.blit(move_right[animation], (player_x, player_y))

        if key[pygame.K_a] and player_x > -30:
            player_x -= player_speed
        elif key[pygame.K_d] and player_x < 1610:
            player_x += player_speed

        if not jump:
            if key[pygame.K_SPACE]:
                jump = True
        else:
            if jump_height >= -20:
                if jump_height > 0:
                    player_y -= jump_height
                else:
                    player_y -= jump_height
                jump_height -= 1
            else:
                jump = False
                jump_height = 20

        if animation == 2:
            animation = 0
        else:
            animation += 1
        background_x -= 5
        if background_x == -1700:
            background_x = 0
        enemy_x -= 15
    else:
        screen.blit(text_ls, (690, 100))
        screen.blit(text_ta, text_ta_hb)

        if text_ta_hb.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            time_now = time()
            game = True
            player_x = 400
            enemy_list.clear()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_tick:
            enemy_list.append(enemy.get_rect(topleft=(1900, random.choice(lst))))

    clock.tick(40)

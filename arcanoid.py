import pygame
import sys
from random import randrange as rnd
from random import choice as rch

width, height = 900, 600
framerate = 60
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arcanoid by MS & MN")
clock = pygame.time.Clock()

#  colors
blue = pygame.transform.scale(pygame.image.load('blue_block.png'), (80, 40)).convert_alpha()
light_blue = pygame.transform.scale(pygame.image.load('light_blue_block.png'), (80, 40)).convert_alpha()
green = pygame.transform.scale(pygame.image.load('green_block.png'), (80, 40)).convert_alpha()
pink = pygame.transform.scale(pygame.image.load('pink_block.png'), (80, 40)).convert_alpha()
red = pygame.transform.scale(pygame.image.load('red_block.png'), (80, 40)).convert_alpha()
yellow = pygame.transform.scale(pygame.image.load('yellow_block.png'), (80, 40)).convert_alpha()
#
colorz = []
for k in range(6):
    for i in range(7):
        colorz.extend((blue, light_blue, red, green, pink, yellow))
colorz.extend((blue, light_blue))
res_cols = colorz

padw = 106
padh = 28
speed = 15
padd = pygame.transform.scale(pygame.image.load('paddle_cr.png'), (padw, padh)).convert_alpha()
paddle = padd.get_rect(center=(450, 575))
#
bg = pygame.image.load('cosmos.jpg')
ball_rad = 15
ball_speed = 6
ball_rect = int(ball_rad * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, width - ball_rect), height // 2, ball_rect, ball_rect)
dx = 1
dy = -1

blocks = [pygame.Rect(10 + 80*i, 10 + 40*j, 80, 40) for i in range(11) for j in range(4)]
res_blocks = blocks

is_going = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(bg, (0, 0))
    #
    if is_going:
        screen.blit(padd, paddle)
        i = 0
        for h in blocks:
            screen.blit(colorz[i], (h.x, h.y))
            i += 1

        pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_rad)
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        key = pygame.key.get_pressed()
        if ball.centery < 15:
            dy = -dy
        if ball.centerx > 885 or ball.centerx < 15:
            dx = -dx
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= speed
        if key[pygame.K_RIGHT] and paddle.right < 900:
            paddle.right += speed

        if ball.colliderect(paddle):
            if dx > 0:
                deltax = ball.right - paddle.left
            else:
                deltax = paddle.right - ball.left
            if dy > 0:
                deltay = ball.bottom - paddle.top
            else:
                deltay = paddle.bottom - ball.top
            if deltax > deltay:
                dy = -dy
            elif deltay > deltax:
                dx = -dx
                dy = -dy
        for block in blocks:
            if ball.colliderect(block):
                if dx > 0:
                    deltax = ball.right - block.left
                else:
                    deltax = block.right - ball.left
                if dy > 0:
                    deltay = ball.bottom - block.top
                else:
                    deltay = block.bottom - ball.top
                if deltax > deltay:
                    dy = -dy
                elif deltay > deltax:
                    dx = -dx
                s = blocks.index(block)
                colorz.pop(s)
                blocks.pop(s)
        #
        if ball.centery > 600:
            is_going = False
            colorz = res_cols
            blocks = res_blocks
    #
    pygame.display.flip()

    clock.tick(framerate)

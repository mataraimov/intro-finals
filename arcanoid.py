import pygame
import sys
from random import randrange as rnd

width, height = 900, 600
framerate = 60

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
padw = 220
padh = 20
speed = 15
paddle = pygame.Rect(320, height - 30, padw, padh)
#
ball_rad = 15
ball_speed = 6
ball_rect = int(ball_rad * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, width - ball_rect), height // 2, ball_rect, ball_rect)
dx = 1
dy = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    #
    pygame.draw.rect(screen, pygame.Color('orange'), paddle)
    pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_rad)
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    key = pygame.key.get_pressed()
    if ball.centerx >= 885 or ball.centerx <= 15:
        dx *= -1
    if ball.centery <= 15 or ball.centery >= 585 or ball.colliderect(paddle):
        dy *= -1
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= speed
    if key[pygame.K_RIGHT] and paddle.right < 900:
        paddle.right += speed
    #
    pygame.display.flip()
    clock.tick(framerate)

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
speed = 7
paddle = pygame.Rect(320, height - 30, padw, padh)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    #
    pygame.draw.rect(screen, pygame.Color('orange'), paddle)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= speed
    if key[pygame.K_RIGHT] and paddle.right < 900:
        paddle.right += speed
    #
    pygame.display.flip()
    clock.tick(framerate)

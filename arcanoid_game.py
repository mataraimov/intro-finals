import pygame
import sys
from random import randrange as rnd
from random import choice as rch


def score_dis(scoree, highscoree):
    if is_going:
        scoresur = game_font.render(f'Score: {scoree}', True, (255, 255, 255))
        score_rect = scoresur.get_rect(center=(800, 400))
        screen.blit(scoresur, score_rect)
    elif not is_going and lost:
        scoresur = game_font2.render(f'Score: {scoree}', True, (255, 255, 255))
        score_rect = scoresur.get_rect(center=(450, 500))
        screen.blit(scoresur, score_rect)

        highscoresur = game_font2.render(f'High score: {highscoree}', True,
                                         (255, 255, 255))
        highscore_rect = highscoresur.get_rect(center=(450, 75))
        screen.blit(highscoresur, highscore_rect)

        highscoresurs = game_font2.render(f'PRESS SPACE TO PLAY AGAIN!', True,
                                          (255, 255, 255))
        highscore_rects = highscoresurs.get_rect(center=(450, 550))
        screen.blit(highscoresurs, highscore_rects)
    elif not is_going and not lost:
        highscoresurse = game_font2.render(f'PRESS SPACE TO GO ON NEXT LEVEL!',
                                           True, (255, 255, 255))
        highscore_rectse = highscoresurse.get_rect(center=(450, 550))
        screen.blit(highscoresurse, highscore_rectse)


width, height = 900, 600
framerate = 60
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arcanoid by MS & MN")
clock = pygame.time.Clock()

#  colors
blue = pygame.transform.scale(pygame.image.load('blue_block.png'),
                              (80, 40)).convert_alpha()
light_blue = pygame.transform.scale(pygame.image.load('light_blue_block.png'),
                                    (80, 40)).convert_alpha()
green = pygame.transform.scale(pygame.image.load('green_block.png'),
                               (80, 40)).convert_alpha()
pink = pygame.transform.scale(pygame.image.load('pink_block.png'),
                              (80, 40)).convert_alpha()
red = pygame.transform.scale(pygame.image.load('red_block.png'),
                             (80, 40)).convert_alpha()
yellow = pygame.transform.scale(pygame.image.load('yellow_block.png'),
                                (80, 40)).convert_alpha()
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
padd = pygame.transform.scale(pygame.image.load('paddle_cr.png'),
                              (padw, padh)).convert_alpha()
paddle = padd.get_rect(center=(450, 575))
#
bg = pygame.image.load('cosmos.jpg')
ball_rad = 15
ball_speed = 5
ball_rect = int(ball_rad * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, width - ball_rect), height // 2, ball_rect,
                   ball_rect)
dx = 1
dy = -1

blocks = [pygame.Rect(10 + 80*i, 10 + 40*j, 80, 40) for i in range(11)
          for j in range(4)]
res_blocks = [pygame.Rect(10 + 80*i, 10 + 40*j, 80, 40) for i in range(11)
              for j in range(4)]

game_font = pygame.font.Font('fb.TTF', 18)
game_font2 = pygame.font.Font('fb.TTF', 32)
score = 0
highscore = 0
points = 1
is_going = True
lost = False
touched = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_going and lost:
                is_going = True
                blocks = [pygame.Rect(10 + 80*i, 10 + 40*j, 80, 40)
                          for i in range(11) for j in range(4)]
                colorz = []
                for k in range(6):
                    for i in range(7):
                        colorz.extend((blue, light_blue, red, green,
                                       pink, yellow))
                colorz.extend((blue, light_blue))

                ball.center = (rnd(ball_rect, width - ball_rect), height // 2)
                dx = 1
                dy = -1
                score = 0
                speed = 15
                ball_speed = 5
                lost = False
            elif event.key == pygame.K_SPACE and not is_going and not lost:
                is_going = True
                blocks = [pygame.Rect(10 + 80*i, 10 + 40*j, 80, 40)
                          for i in range(11) for j in range(4)]
                colorz = []
                for k in range(6):
                    for i in range(7):
                        colorz.extend((blue, light_blue, red, green, pink,
                                       yellow))
                colorz.extend((blue, light_blue))

                ball.center = (rnd(ball_rect, width - ball_rect), height // 2)
                dx = 1
                dy = -1
                points *= 2
                speed += 2
                ball_speed += 2
    screen.blit(bg, (0, 0))
    #
    if is_going:
        screen.blit(padd, paddle)
        i = 0
        for h in blocks:
            screen.blit(colorz[i], (h.x, h.y))
            i += 1

        pygame.draw.circle(screen, pygame.Color('white'), ball.center,
                           ball_rad)
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        key = pygame.key.get_pressed()
        if ball.centery < 15:
            dy = -dy
            touched = False
        if ball.centerx > 885 or ball.centerx < 15:
            dx = -dx
            touched = False
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= speed
        if key[pygame.K_RIGHT] and paddle.right < 900:
            paddle.right += speed

        if ball.colliderect(paddle) and not touched:
            if dx > 0:
                deltax = ball.right - paddle.left
            else:
                deltax = paddle.right - ball.left
            if dy > 0:
                deltay = ball.bottom - paddle.top
            else:
                deltay = paddle.bottom - ball.top
            if abs(deltax - deltay) < 10:
                dx, dy = -dx, -dy
            elif deltax > deltay:
                dy = -dy
            elif deltay > deltax:
                dx = -dx
                dy = -dy
            touched = True
        for block in blocks:
            if ball.colliderect(block):
                if dx > 0:
                    deltax = ball.right - paddle.left
                else:
                    deltax = paddle.right - ball.left
                if dy > 0:
                    deltay = ball.bottom - paddle.top
                else:
                    deltay = paddle.bottom - ball.top
                if abs(deltax - deltay) < 10:
                    dx, dy = -dx, -dy
                elif deltax > deltay:
                    dy = -dy
                elif deltay > deltax:
                    dx = -dx
                    dy = -dy
                s = blocks.index(block)
                colorz.pop(s)
                blocks.pop(s)
                score += points
                touched = False

        #
        if ball.bottom >= 600:
            is_going = False
            touched = False
            lost = True

        if len(blocks) == 0:
            is_going = False
            lost = False

        if highscore < score:
            highscore = score
        score_dis(score, highscore)

    if not is_going and lost:
        gameover = pygame.image.load('gameover.png').convert_alpha()
        gameover_rect = gameover.get_rect(center=(450, 300))
        screen.blit(gameover, gameover_rect)
        score_dis(score, highscore)
    elif not is_going:
        gratz = pygame.image.load('gratz.png').convert_alpha()
        gratz_rect = gratz.get_rect(center=(450, 300))
        screen.blit(gratz, gratz_rect)
        score_dis(score, highscore)
    #

    pygame.display.flip()

    clock.tick(framerate)

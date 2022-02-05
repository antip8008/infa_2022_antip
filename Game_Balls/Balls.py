import pygame
from pygame.draw import *
from random import randint
from math import sin, cos

points = 0
sec = 0

screen = pygame.display.set_mode((1350, 700))
pygame.display.set_caption(' Game: Balls')

pygame.init()

SEC = 60   # время игры в секундах
FPS = 90

FRAME_LIMIT = SEC * FPS   # лимит фреймов
FRAME_CURRENT = 0         # номер текущего фрейма

dis_width = 1350
dis_height = 700
dis = pygame.display.set_mode((dis_width, dis_height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

x = 0
y = 0
r = 0
color = 0
steps = 0
corner = randint(0, 360)

def Your_time():
    global FRAME_CURRENT, FPS
    value = score_font.render("Your Time: " + str(round(FRAME_CURRENT / FPS)), True, BLUE)
    dis.blit(value, [580, 0])


def Your_score():
    global points
    value = score_font.render("Your Score: " + str(points), True, YELLOW)
    dis.blit(value, [0, 0])


def message(msg, clr, x=2, y=3):
    global dis_width, dis_height
    msg = font_style.render(msg, True, clr)
    dis.blit(msg, [dis_width / x - msg.get_width() / 2, dis_height / y])


def new_ball():
    global x, y, r, color
    x = randint(100, 1250)
    y = randint(100, 600)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


deltaX = 10
deltaY = 10


def move_ball():
    global x, y, r, color, steps, deltaX, deltaY
    x += deltaX * sin(corner)
    y += deltaY * cos(corner)
    if x > 1320 or x < 30:
        deltaX *= -1
    if y < 30 or y > 670:
        deltaY *= -1

    circle(screen, color, (x, y), r)
    steps += 1


def click(event):
    global points, corner
    X, Y = event.pos
    if (Y - y) ** 2 + (X - x) ** 2 <= r ** 2:
        points += 1
        corner = randint(0, 360)
        new_ball()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()

while not finished:
    clock.tick(FPS)
    FRAME_CURRENT += 1
    move_ball()
    Your_score()
    Your_time()
    if FRAME_CURRENT > FRAME_LIMIT:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    pygame.display.update()
    screen.fill(BLACK)


message("GAME OVER!", RED)
message("Press Q to quit", GREEN, y=2)
pygame.display.update()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                finished = True

pygame.quit()

# игра проходит на шахматной доске
# фигуры на доске черные и белые шашки
# при попытке слопать шашку открывается мини игра (камень, ножницы, бумага)
# победитель мини игры занимает места сраженной шашки
# игра идет до полного уничтожения фишек противника

import pygame
import sys
from doska import Doska


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption('Crazy Checkers')
    bg_color = (10, 50, 50)
    dosca = Doska(screen)

    pygame.mixer.music.load('sound/INTERSTELLAR.mp3')
    pygame.mixer.music.play(-1)
    pygame.image.load('images/doska.png').convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        dosca.output()
        pygame.display.flip()


run()

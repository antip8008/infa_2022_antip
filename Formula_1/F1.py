import controls
import pygame
from pygame.sprite import Group

from bollid import Bollid
from trek import Cherta


def run():
    clock = pygame.time.Clock()
    FPS = 40

    pygame.init()
    screen = pygame.display.set_mode((600, 690))
    pygame.display.set_caption('F1')
    pygame.mixer.music.load('sound/F1trek.mp3')
    pygame.mixer.music.play(-1)
    bg_color = (158, 158, 158)
    bollid = Bollid(screen)
    cherts = Group()

    c = Cherta(300, bollid)
    cherts.add(c)

    while True:
        clock.tick(FPS)
        controls.event(bollid)

        cherts.update()

        screen.fill(bg_color)

        cherts.draw(screen)
        bollid.output()
        pygame.display.flip()


run()

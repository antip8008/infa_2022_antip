import pygame
from bollid import Bollid
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 690))
    pygame.display.set_caption('F1')
    bg_color = (0, 0, 0)
    bollid = Bollid(screen)
    cherti = Group

    while True:



        screen.fill(bg_color)
        bollid.output()
        pygame.display.flip()

run()




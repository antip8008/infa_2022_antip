import time

import pygame
from os import path

class Bollid(pygame.sprite.Sprite):

    speed: int = 0
    accelerate = 0
    fr: int = 0


    def __init__(self, screen):
        """инициализация гонки"""

        super().__init__()
        self.screen = screen
        self.imege = pygame.image.load('imege/f.png')
        self.rect = self.imege.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.explosion_anim = []
        img_dir = path.join(path.dirname(__file__), 'imege')
        for i in range(0, 10):
            filename = '0{}.png'.format(i)
            img = pygame.image.load(path.join(img_dir, filename)).convert()
            img.set_colorkey((0, 0, 0))
            img_lg = pygame.transform.scale(img, (75, 75))
            self.explosion_anim.append(img_lg)
        self.explosion = None

        self.speed = 10

    def restart(self):
        time.sleep(5)
        self.rect.centerx = self.screen_rect.centerx
        self.explosion = None
        self.imege = pygame.image.load('imege/f.png')
        self.speed = 10

    def output(self):
        if self.explosion is not None:
            self.draw_pizdets()
        self.fr += 1
        if self.fr >= 1000:
            self.speed += 3
            self.fr = 0

        self.screen.blit(self.imege, self.rect)

    def pizdets(self):
        self.speed = 0
        self.explosion = -1


    def draw_pizdets(self):
        if self.explosion < len(self.explosion_anim) - 1:
            self.explosion += 1
            self.imege = self.explosion_anim[self.explosion]
        else:
            self.restart()

    def screen(self):
        return self.s


class Enemy(pygame.sprite.Sprite):

    def __init__(self, bollid: Bollid):
        super().__init__()
        self.bollid = bollid

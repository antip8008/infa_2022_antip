import pygame
from bullet import Bullet
from datetime import datetime


class Penis:
    def __init__(self, screen):
        """инициализация пушки"""

        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mup = False
        self.is_cuming = False
        self.last_cumshot = datetime.now()
        self.cooldown = 0.1

    def begin_cum(self):
        self.is_cuming = True

    def end_cum(self):
        self.is_cuming = False

    def cum(self):
        if (datetime.now() - self.last_cumshot).total_seconds() >= self.cooldown:
            self.last_cumshot = datetime.now()
            return Bullet(self.screen, self)
        return None

    def output(self):
        """рисует пушку"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции"""
        if self.mright and self.rect.right < self.screen_rect.right + 30:
            self.center += .8
        if self.mleft and self.rect.left > - 30:
            self.center -= .8
        self.rect.centerx = self.center
        if self.is_cuming:
            return self.cum()
        return None

    def create_gun(self):
        """возобновляет пушку"""
        self.center = self.screen_rect.centerx
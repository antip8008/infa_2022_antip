import pygame


class Doska:
    def __init__(self, screen):
        """инициализация доску"""

        self.screen = screen
        self.image = pygame.image.load('images/doska.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.x + 50
        self.rect.bottom = self.screen_rect.bottom - 25

    def output(self):
        """рисует доску"""
        self.screen.blit(self.image, self.rect)

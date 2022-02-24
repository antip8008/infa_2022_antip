import pygame

class Bollid:
    def __init__(self, screen):
        """инициализация гонки"""

        self.screen = screen
        self.imege = pygame.image.load('imege/f.png')
        self.rect = self.imege.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def output(self):
        """рисует пушку"""
        self.screen.blit(self.imege, self.rect)

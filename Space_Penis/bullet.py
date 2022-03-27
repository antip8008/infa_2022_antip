import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создаем пулю"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = 255, 255, 255
        self.speed = 5
        self.rect.centerx = gun.rect.centerx - 5
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """движение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)

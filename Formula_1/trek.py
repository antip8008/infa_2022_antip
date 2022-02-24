import pygame

class Cherta(pygame.sprite.Sprite):
    def __init__(self, screen):
        """создаем линию"""
        super(Cherta, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(200, 690, 10, 50)
        self.rect = pygame.Rect(400, 690, 10, 50)
        self.color = (0, 0, 0,)
        self.speed = 10
        self.y = float(self.rect.y)


    def update(self):
        """перемещение линий вниз"""
        self.y -= self.speed
        self.rect.y = self.y


    def draw_cherta(self):
        """рисует черту на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)



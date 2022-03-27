import pygame


class Cherta(pygame.sprite.Sprite):

    def __init__(self, offset_x: int, bollid):
        """создаем линию"""
        super(Cherta, self).__init__()
        self.bollid = bollid
        self.image = pygame.Surface((600, 850))
        self.image.fill((31, 34, 36))
        # x = [0, 596]
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, 4, 790))
        pygame.draw.rect(self.image, (255, 255, 255), (596, 0, 4, 790))

        y = 0
        while y < 790:
            for x in [198, 398]:
                h = 40
                pygame.draw.rect(self.image, (255, 255, 255), pygame.Rect(x, y, 4, h))
            y += 100

        self.rect = self.image.get_rect()
        self.rect.centerx = offset_x
        self.rect.y = -100
        self.y_start = self.rect.y

    def update(self):
        """перемещение линий вниз"""

        self.rect.y += self.bollid.speed
        if self.rect.y >= 0:
            self.rect.y = -100

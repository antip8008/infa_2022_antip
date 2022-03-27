import pygame
from pygame.draw import *
pygame.init()

FPS = 30
#фон
screen = pygame.display.set_mode((600, 700))
rect(screen, (30, 50, 0), (0, 350, 700, 350))
rect(screen, (0, 20, 30), (0, 0, 700, 350))
#луна
circle(screen, (255, 255, 255), (420, 150), 95)

#элипс облока
ellipse(screen, (105,105,105),(-170,10,550,120))
ellipse(screen, (105,105,105),(370,-30,450,90))
ellipse(screen, (105,105,105),(330,70,550,80))
ellipse(screen, (105,105,105),(-30,140,450,80))
ellipse(screen, (105,105,105),(290,170,450,90))
ellipse(screen, (50,50,50),(190,50,450,80))
ellipse(screen, (50,50,50),(200,210,450,80))
ellipse(screen, (50,50,50),(-160,110,450,70))


#свет
surface = pygame.surface.Surface(screen.get_size()).convert_alpha()
pygame.draw.polygon(surface, (255, 255, 255), [(135,280), (30,460), (260,460)])

surface.set_alpha(64)
screen.blit(surface, (0,0))

#тарелка
surface2 = pygame.surface.Surface(screen.get_size()).convert_alpha()
surface2.fill([0, 0, 0, 0])
surface2.set_colorkey([0,0,0])
ellipse(surface2, (140,140,132),(10,240,260,80))
ellipse(surface2, (192,192,192),(55,230,170,50))
ellipse(surface2, (255,255,255),(25,270,30,15))
ellipse(surface2, (255,255,255),(55,285,30,15))
ellipse(surface2, (255,255,255),(97,292,30,15))
ellipse(surface2, (255,255,255),(142,292,30,15))
ellipse(surface2, (255,255,255),(184,286,30,15))
ellipse(surface2, (255,255,255),(220,270,30,15))

#амонгас
#тулово
pygame.draw.line(surface2, (255,0,0),(350,450),(350,600),10)
pygame.draw.line(surface2, (255,0,0),(438,450),(438,600),10)
pygame.draw.line(surface2, (255,0,0),(410,450),(410,600),10)
pygame.draw.line(surface2, (255,0,0),(378,450),(378,600),10)
rect(surface2, (255, 0, 0), (350, 480, 30, 100))
rect(surface2, (255, 0, 0), (410, 480, 30, 100))
rect(surface2, (255, 0, 0), (380, 445, 30, 100))
ellipse(surface2, (255,0,0),(345,414,100,100))
ellipse(surface2, (255,0,0),(345,572,40,40))
ellipse(surface2, (255,0,0),(375,540,40,40))
ellipse(surface2, (255,0,0),(405,572,40,40))
#очки
ellipse(surface2, (0,255,255),(420,450,40,40))
ellipse(surface2, (0,255,255),(380,450,40,40))
rect(surface2, (0, 255, 255), (380, 450, 55, 40))
#ранец
rect(surface2, (0, 255, 255), (317, 470, 30, 90))

screen.blit(surface2, (0,0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
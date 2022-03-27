import pygame
import sys



def event(bollid):
    """обработка событий"""
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_d:
                if bollid.rect.centerx < 301:
                    bollid.rect.centerx += 200
                else:
                   bollid.pizdets()
            # влраво
            if events.key == pygame.K_a:
                if bollid.rect.centerx > 299:
                    bollid.rect.centerx -= 200
                else:
                   bollid.pizdets()








def update2(bg_color, screen, bollid):
    screen.fill(bg_color)
    bollid.output()
    pygame.display.flip()

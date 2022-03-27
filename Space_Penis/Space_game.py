import controls
import pygame
from pygame.sprite import Group
from penis import Penis
from stats import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 690))
    pygame.display.set_caption("Космические Членовойны")
    bg_color = (0, 0, 0)
    gun = Penis(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()

    while True:
        controls.events(gun)
        new_bullet = gun.update_gun()
        if new_bullet:
            bullets.add(new_bullet)
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(screen, inos, bullets)
        controls.update_inos(stats, screen, gun, inos, bullets)


run()

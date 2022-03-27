import pygame
import sys
from ino import Ino
import time

fire = False


def events(gun):
    """обработка событий"""
    global fire
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            # выстрел
            elif event.key == pygame.K_SPACE:
                gun.begin_cum()
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = False
            elif event.key == pygame.K_SPACE:
                gun.end_cum()


def update(bg_color, screen, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, inos, bullets):
    """обновляет позицию пули"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def update_inos(stats, screen, gun, inos, bullets):
    """обновляет позицию прешельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_lill(stats, screen, gun, inos, bullets)
    inos_check(stats, screen, gun, inos, bullets)


def inos_check(stats, screen, gun, inos, bullets):
    """проверка добралась ли армия до пушки"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_lill(stats, screen, gun, inos, bullets)
            break


def gun_lill(stats, screen, gun, inos, bullets):
    """столкновение пушки и пришельцев"""
    stats.guns_left -= 1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    gun.create_gun()
    time.sleep(2)


def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((600 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((690 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 10):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x + 12.5
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)


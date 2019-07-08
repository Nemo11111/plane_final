import sys
import time
import pygame

from enemy import Enemy
from pygame import camera


def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True
    elif event.key == pygame.K_SPACE:
        player.onFire = True


def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False
    elif event.key == pygame.K_SPACE:
        player.onFire = False


def update_screen(settings, screen, player, enemies, bullets, bullets_enemy):
    screen.fill(settings.bg_color)

    player.blitme()
    enemies.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets_enemy.sprites():
        bullet.draw_bullet()

    pygame.display.flip()



def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def update_enemies(enemies):
    enemies.update()


def check_collision(player, enemies, bullets, bullets_enemy):
    pygame.sprite.groupcollide(enemies, bullets, True, True)
    collide_list = pygame.sprite.spritecollide(player, bullets_enemy, False)
    if len(collide_list) > 0:
        return True
    return False


def create_enemy(settings, screen, enemies, level, bullets):
    enemy = Enemy(settings, screen, bullets, level)
    enemies.add(enemy)


def sync():
    time.sleep(0.016)

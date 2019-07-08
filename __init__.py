import threading
from numpy import *
import pygame
from pygame.sprite import Group
import pygame.surfarray

import functions as functs
from settings import Settings
from player import Player

pygame.init()
settings = Settings()
screen:pygame.Surface = pygame.display.set_mode(
    (settings.screen_width, settings.screen_height))

pygame.display.set_caption("Plane")

level = 1
cycle = 0
coldDownTime = 50
leftColdDownTime = 0

bullets = Group()
bullets_enemy = Group()
enemies = Group()

player = Player(settings, screen, bullets)



def run_game():
    global settings
    global screen

    global level
    global cycle
    global coldDownTime
    global leftColdDownTime

    global bullets
    global bullets_enemy
    global enemies

    global player

    while True:
        while True:
            sync = threading.Thread(target=functs.sync, args=())
            sync.start()

            functs.check_events(player)

            player.update()
            functs.update_bullets(bullets)
            functs.update_bullets(bullets_enemy)
            functs.update_enemies(enemies)

            if functs.check_collision(player, enemies, bullets, bullets_enemy):
                break

            functs.update_screen(settings, screen, player, enemies, bullets, bullets_enemy)

            cycle += 1
            if cycle == 300:
                level += 1
                cycle = 0
                arr = pygame.surfarray.array2d(screen)
                print(arr)

            if len(enemies) < level and leftColdDownTime <= 0:
                functs.create_enemy(settings, screen, enemies, level, bullets_enemy)
                leftColdDownTime = coldDownTime - level
            leftColdDownTime -= 1


            sync.join()
        pygame.init()
        settings = Settings()
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Plane")

        level = 1
        cycle = 0

        bullets = Group()
        bullets_enemy = Group()
        enemies = Group()

        player = Player(settings, screen, bullets)

run_game()




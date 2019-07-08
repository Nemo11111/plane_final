import pygame
import pygame.surfarray
from pygame.sprite import Group

import functions as functs
from settings import Settings
from player import Player


class PlaneEnv:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen:pygame.Surface = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Plane")

        self.level = 1
        self.cycle = 0
        self.coldDownTime = 50
        self.leftColdDownTime = 0

        self.bullets = Group()
        self.bullets_enemy = Group()
        self.enemies = Group()

        self.player = Player(self.settings, self.screen, self.bullets)

    def step(self, action):
        if action == 0:
            self.player.onFire = True
        elif action == 1:
            self.player.onFire = False
        elif action == 2:
            self.player.moving_left = True
        elif action == 3:
            self.player.moving_left = False
        elif action == 4:
            self.player.moving_right = True
        elif action == 5:
            self.player.moving_right = False
        elif action == 6:
            self.player.moving_up = True
        elif action == 7:
            self.player.moving_up = False
        elif action == 8:
            self.player.moving_down = True
        elif action == 9:
            self.player.moving_down = False

        reward, done = self.update()
        next_obs = pygame.surfarray.array2d(self.screen)

        return next_obs, reward, done, {}

    def reset(self):
        self.level = 1
        self.cycle = 0
        self.coldDownTime = 50
        self.leftColdDownTime = 0

        self.bullets = Group()
        self.bullets_enemy = Group()
        self.enemies = Group()

        self.player = Player(self.settings, self.screen, self.bullets)

    def render(self):
        functs.update_screen(self.settings, self.screen,
                             self.player, self.enemies,
                             self.bullets, self.bullets_enemy)

    def close(self):
        return

    def update(self):
        self.player.update()
        functs.update_bullets(self.bullets)
        functs.update_bullets(self.bullets_enemy)
        functs.update_enemies(self.enemies)

        reward = 0
        done = False
        enemies_collision = \
            pygame.sprite.groupcollide(self.enemies,
                                       self.bullets, True, True)
        for enemy in enemies_collision:
            reward += enemy.level

        player_collision = \
            pygame.sprite.spritecollide(self.player,
                                        self.bullets_enemy, False)
        if len(player_collision) > 0:
            reward -= 100
            done = True

        self.cycle += 1
        if self.cycle == 300:
            self.level += 1
            self.cycle = 0

        if len(self.enemies) < self.level \
                and self.leftColdDownTime <= 0:
            functs.create_enemy(self.settings, self.screen,
                                self.enemies, self.level,
                                self.bullets_enemy)
            self.leftColdDownTime = self.coldDownTime - self.level
        self.leftColdDownTime -= 1

        return reward, done

import pygame
from pygame.sprite import Sprite
import random


class Bullet(Sprite):
    def __init__(self, settings, screen, entity, direction):
        super(Bullet, self).__init__()
        self.settings = settings
        self.screen = screen
        self.entity = entity
        self.direction = direction

        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centerx = entity.rect.centerx
        if direction == -1:
            self.horizontal = 0
            self.rect.centerx = entity.rect.centerx
            self.rect.top = entity.rect.top
        elif direction == 1:
            self.horizontal = 1 if random.uniform(-1, 1) > 0 else -1
            self.rect.centerx = entity.rect.centerx
            self.rect.bottom = entity.rect.bottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        if direction == -1:
            self.color = settings.bullet_color_player
        elif direction == 1:
            self.color = settings.bullet_color_enemy

        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        self.y += self.direction * self.speed_factor
        self.rect.y = self.y
        self.rect.x += self.horizontal

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

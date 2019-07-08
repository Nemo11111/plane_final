import pygame


class Settings:
    def __init__(self):
        self.screen_width = 100
        self.screen_height = 100
        self.bg_color = (255, 255, 255)

        self.plane_speed_factor = 6
        self.bullet_speed_factor = 8
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color_player = 0, 0, 255
        self.bullet_color_enemy = 255, 0, 0

        self.enemy_speed_factor = 4

        self.player_image = pygame.image.load('images/player.bmp')
        self.enemy_image = pygame.image.load('images/enemy.bmp')

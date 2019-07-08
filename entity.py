import pygame
from pygame.sprite import Sprite

class Entity(Sprite):
    def __init__(self, settings, screen):
        super(Entity, self).__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

    def blitme(self):
        pass


    def update(self):
        pass
    
    
    def fire(self):
        pass
    
    
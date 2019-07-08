from entity import Entity
from bullet import Bullet


class Player(Entity):

    def __init__(self, settings, screen, bullets):
        super(Player, self).__init__(settings, screen)
        self.bullets = bullets

        self.image = settings.player_image
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.onFire = False
        self.coldDownTime = 5
        self.leftColdDownTime = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.plane_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.plane_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.plane_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.plane_speed_factor

        if self.leftColdDownTime != 0:
            self.leftColdDownTime -= 1
        if self.onFire:
            self.fire()

    def fire(self):
        if self.leftColdDownTime > 0:
            return
        self.leftColdDownTime = self.coldDownTime

        new_bullet = Bullet(self.settings, self.screen, self, -1)
        self.bullets.add(new_bullet)

import random
from entity import Entity
from bullet import Bullet


class Enemy(Entity):
    def __init__(self, settings, screen, bullets, level):
        super(Enemy, self).__init__(settings, screen)
        self.bullets = bullets
        self.level = level

        self.image = settings.enemy_image
        self.rect = self.image.get_rect()

        self.rect.x = random.uniform(0+self.rect.width, screen.get_rect().width-self.rect.width)
        self.rect.y = random.uniform(0+self.rect.width, screen.get_rect().centery-self.rect.height)
        self.direction = 1 if random.uniform(-1, 1) > 0 else -1

        self.coldDownTime = 8
        self.leftColdDownTime = 0
        self.bigcoldDownTime = 120
        self.leftBulletsNum = self.level

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.leftColdDownTime > 0:
            self.leftColdDownTime -= 1
        self.fire()

        if self.direction == 1:
            self.rect.x += self.settings.enemy_speed_factor
            if self.rect.right >= self.screen_rect.width:
                self.direction = -1
        else:
            self.rect.x -= self.settings.enemy_speed_factor
            if self.rect.left <= 0:
                self.direction = 1

        self.bigcoldDownTime -= 1
        if self.bigcoldDownTime <= 0:
            self.bigcoldDownTime = 120
            self.leftBulletsNum = self.level

    def fire(self):
        if self.leftColdDownTime > 0 or self.leftBulletsNum <= 0:
            return

        self.leftColdDownTime = self.coldDownTime
        self.leftBulletsNum -= 1
        new_bullet = Bullet(self.settings, self.screen, self, 1)
        self.bullets.add(new_bullet)

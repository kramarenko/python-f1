import pygame
import bullet
from os import path


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, powerup_time):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = self.load_image()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width / 2
        self.rect.bottom = self.height - 10
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.shoot_delay = 250
        self.powerup_time = powerup_time
        self.last_shot = pygame.time.get_ticks()
        self.bullets = pygame.sprite.Group()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def load_image(self):
        img_dir = path.join(path.dirname(__file__), 'img')
        image = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
        image = pygame.transform.scale(image, (50, 38))
        image.set_colorkey((0, 0, 0))
        return image

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if keystate[pygame.K_SPACE]:
            self.shoot()

        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.left < 0:
            self.rect.left = 0

        # if keystate[pygame.K_UP]:
        #     self.speedy = -8
        # if keystate[pygame.K_DOWN]:
        #     self.speedy = 8
        # self.rect.y += self.speedy
        #
        # if self.rect.bottom > self.height:
        #     self.rect.bottom = self.height
        # if self.rect.top < 0:
        #     self.rect.top = 0
        self.show()
        self.bullets.update()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                blt = bullet.Bullet(self.rect.centerx, self.rect.top)
                # all_sprites.add(bullet)
                blt.play()
                self.bullets.add(blt)
            if self.power >= 2:
                bullet1 = bullet.Bullet(self.rect.left, self.rect.centery)
                bullet2 = bullet.Bullet(self.rect.right, self.rect.centery)
                # all_sprites.add(bullet1)
                # all_sprites.add(bullet2)
                self.bullets.add(bullet1)
                self.bullets.add(bullet2)
                bullet1.play()


    def get_bullet(self):
        return self.bullets

    def draw(self, screen):
        self.bullets.draw(screen)

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.width / 2, self.height + 200)

    def show(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = self.width / 2
            self.rect.bottom = self.height - 10

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def activate_power(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > self.powerup_time:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

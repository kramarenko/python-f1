import pygame
import random
from os import path


class Pow(pygame.sprite.Sprite):
    def __init__(self, center, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.width = width
        self.height = height
        self.image = self.load_image()[self.type]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # убить, если он сдвинется с нижней части экрана
        if self.rect.top > self.height:
            self.kill()

    def load_image(self):
        img_dir = path.join(path.dirname(__file__), 'img')
        powerup_images = {}
        powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
        powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()
        return powerup_images

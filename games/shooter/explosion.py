import pygame
from os import path


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.explosion_anim = self.load_images()
        self.image = self.explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def load_images(self):
        explosion_anim = {}
        explosion_anim['lg'] = []
        explosion_anim['sm'] = []
        explosion_anim['player'] = []
        for i in range(9):
            img_dir = path.join(path.dirname(__file__), 'img/explode')
            filename = 'regularExplosion0{}.png'.format(i)
            img = pygame.image.load(path.join(img_dir, filename)).convert()
            img.set_colorkey((0, 0, 0))
            img_lg = pygame.transform.scale(img, (75, 75))
            explosion_anim['lg'].append(img_lg)
            img_sm = pygame.transform.scale(img, (32, 32))
            explosion_anim['sm'].append(img_sm)
            filename = 'sonicExplosion0{}.png'.format(i)
            img = pygame.image.load(path.join(img_dir, filename)).convert()
            img.set_colorkey((0, 0, 0))
            explosion_anim['player'].append(img)

        return explosion_anim

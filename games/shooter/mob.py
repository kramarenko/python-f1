import pygame
import random
from os import path


class Mob(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.expl_sounds = self.load_sound()
        self.image_orig = self.load_image()
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, (255, 0, 0) , self.rect.center, self.radius)
        self.rect.x = random.randrange(self.width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def load_image(self):
        img_dir = path.join(path.dirname(__file__), 'img')

        meteor_images = []
        meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
                       'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
                       'meteorBrown_tiny1.png']
        for img in meteor_list:
            meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

        image_orig = random.choice(meteor_images)
        image_orig.set_colorkey((0, 0, 0))
        return image_orig

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > self.height + 10 or self.rect.left < -25 or self.rect.right > self.width + 20:
            self.rect.x = random.randrange(self.width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.rotate()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def load_sound(self):
        sound_dir = path.join(path.dirname(__file__), 'sound')
        expl_sounds = []
        for snd in ['expl3.wav', 'expl6.wav']:
            expl_sounds.append(pygame.mixer.Sound(path.join(sound_dir, snd)))
        return expl_sounds

    def explode(self):
        random.choice(self.expl_sounds).play()
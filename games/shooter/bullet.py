import pygame
from os import path


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.shoot_sound = self.load_sound()
        self.image = self.load_image()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def load_image(self):
        img_dir = path.join(path.dirname(__file__), 'img')
        image = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
        image = pygame.transform.scale(image, (8, 38))
        image.set_colorkey((0, 0, 0))
        return image

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()

    def load_sound(self):
        sound_dir = path.join(path.dirname(__file__), 'sound')
        shoot_sound = pygame.mixer.Sound(path.join(sound_dir, 'pew.wav'))
        return shoot_sound

    def play(self):
        self.shoot_sound.play()


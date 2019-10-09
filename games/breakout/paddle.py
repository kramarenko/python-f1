import pygame


class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, display):
        pygame.draw.rect(display, [255, 255, 255], [self.x, self.y, self.width, self.height])

    def move(self, mouseX):
        self.x = mouseX - self.width / 2



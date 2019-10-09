import pygame


class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, display):
        pygame.draw.rect(display, [104, 149, 186], [self.x, self.y, self.width, self.height])

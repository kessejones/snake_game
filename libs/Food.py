from .GameObject import *
import pygame
import random

class Food(GameObject):

    def __init__(self, display, pos_x, pos_y, size_x, size_y):
        super(Food, self).__init__(display, pos_x, pos_y, size_x, size_y)
        self.cor = self.generate_color()

    def update(self):
        self.cor = self.generate_color()
        self.pos_x = random.randrange(0, 640, 20)
        self.pos_y = random.randrange(0, 320, 20)


    def render(self):
        pygame.draw.rect(self.display, self.cor , pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y))

    def generate_color(self):
        color = (0,0,0)
        while ''.join(map(str,color)) == '000':
            red = random.randrange(0, 255)
            green = random.randrange(0, 255)
            blue = random.randrange(0, 255)

            color = (red, green, blue)
        return color
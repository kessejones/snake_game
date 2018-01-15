from .GameObject import *
import pygame
from enum import Enum
import random

class DirectionSnake(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake(GameObject):

    def __init__(self, display, size_x, size_y, pos_x=0, pos_y=0):
        super(Snake, self).__init__(display, pos_x, pos_y, size_x, size_y)
        self.direction = DirectionSnake.RIGHT
        self.speed = 20
        self.length = []

    def set_speed(self, speed):
        self.speed = speed

    def set_direction(self, direction):
        self.direction = direction

    def set_speed(self, speed):
        self.speed = speed

    def update(self):

        if len(self.length) > 0:
            self.length.insert(0, [self.pos_x, self.pos_y])
            self.length.pop(len(self.length) -1)


        if self.direction == DirectionSnake.UP:
            self.pos_y -= self.speed
        elif self.direction == DirectionSnake.DOWN:
            self.pos_y += self.speed
        elif self.direction == DirectionSnake.LEFT:
            self.pos_x -= self.speed
        elif self.direction == DirectionSnake.RIGHT:
            self.pos_x += self.speed

        print self.length

    def render(self):
        pygame.draw.rect(self.display, (255,255,255), pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y))
        pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y),
                         1)

        for l in self.length:
            pygame.draw.rect(self.display, (255,255,255),
                             pygame.Rect(l[0], l[1], self.size_x, self.size_y))
            pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(l[0], l[1], self.size_x, self.size_y),
                             1)

    def eat(self):
        count = len(self.length)
        if count == 0:
            self.length.append([self.pos_x + self.size_x, self.pos_y + self.size_y])
        else:
            self.length.append([self.length[count - 1][0] + self.size_x, self.length[count - 1][1] + self.size_y])

    def spawn(self):
        self.pos_x = random.randrange(0, 620, 20)
        self.pos_y = random.randrange(0, 300, 20)
        self.length = []

        rand_direction = random.randrange(1, 4)
        self.direction = DirectionSnake(rand_direction)

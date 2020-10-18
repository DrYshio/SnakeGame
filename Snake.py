import pygame


class Snake:
    def __init__(self):
        self.head = [330, 231]
        self.body = [[330, 220], [330, 211]]
        self.score = 0

    def move(self, control):
        if control.direction == 1:
            self.head[0] += 11
        elif control.direction == 2:
            self.head[0] -= 11
        elif control.direction == 3:
            self.head[1] -= 11
        elif control.direction == 4:
            self.head[1] += 11

    def draw_snake(self, surf):
        for segment in self.body:
            pygame.draw.rect(surf, pygame.Color('Green'), pygame.Rect(segment[0], segment[1], 10, 10))
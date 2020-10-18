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

    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def check_board(self):
        if self.head[0] == 649:
            self.head[0] = 11
        elif self.head[0] == 0:
            self.head[0] = 638
        elif self.head[1] == 0:
            self.head[1] = 451
        elif self.head[1] == 462:
            self.head[1] = 11

    def eat(self, food):
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position()
            self.score += 1

    def check_death(self):
        if self.head in self.body:
            self.score = 0

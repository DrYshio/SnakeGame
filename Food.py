import pygame
import random


class Food:
    def __init__(self):

        self.food_position = []
        self.food_position.append(random.randrange(0, 649, 11))
        self.food_position.append(random.randrange(0, 462, 11))

    def get_food_position(self):
        self.food_position[0] = random.randrange(0, 649, 11)
        self.food_position[1] = random.randrange(0, 462, 11)
        print(self.food_position)

    def draw_food(self, surf):
        pygame.draw.rect(surf, pygame.Color('Green'), pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))
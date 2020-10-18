import pygame

from Snake import Snake

# game window parameters
WIDTH = 660
HEIGHT = 473

snake = Snake()


def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cool Snake')

    while True:
        window.fill(pygame.Color('Black'))

        snake.draw_snake(window)


main()

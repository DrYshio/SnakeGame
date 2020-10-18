import pygame


# game window parameters
WIDTH = 660
HEIGHT = 473


def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cool Snake')

    while True:
        window.fill(pygame.Color('Black'))


main()

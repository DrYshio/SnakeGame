import pygame

from Snake import Snake
from Control import Control
from Food import Food
from Gui import Gui

# game window parameters
WIDTH = 660
HEIGHT = 473

pygame.init()

control = Control()
snake = Snake()
food = Food()
gui = Gui()


def main():

    var = 0
    width = 660
    height = 473
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Cool Snake')
    font = pygame.font.SysFont('arial', 32)

    while control.flag:
        window.fill(pygame.Color('Black'))

        text = font.render('Score:' + str(snake.score), True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (10, 420)
        window.blit(text, textRect)
        gui.draw_level(window)
        control.control()
        snake.draw_snake(window)
        food.draw_food(window)

        if var % 30 == 0 and control.flag_pause:
            snake.move(control)
            snake.check_board()
            snake.check_death()
            snake.animation()
            snake.eat(food)
        var += 1
        pygame.display.update()

main()

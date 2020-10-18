import pygame


class Control:
    def __init__(self):
        self.flag = True
        self.direction = 3
        self.flag_pause = True

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.flag = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.direction != 2:
                    self.direction = 1
                elif event.key == pygame.K_LEFT and self.direction != 1:
                    self.direction = 2
                elif event.key == pygame.K_UP and self.direction != 4:
                    self.direction = 3
                elif event.key == pygame.K_DOWN and self.direction != 3:
                    self.direction = 4
                elif event.key == pygame.K_ESCAPE:
                    self.flag = False
                elif event.key == pygame.K_SPACE:
                    if self.flag_pause:
                        self.flag_pause = False
                    elif not self.flag_pause:
                        self.flag_pause = True

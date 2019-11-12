import pygame
from Stick import Stick

class Sticks(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)

        # BadAss hardcoded for 720 resolution
        size = (3, 5, 7)
        delta_x = [215 , 150, 90]
        delta_space = (40, 40, 40)
        y = 5

        for i in range(len(size)):
            level = size[i]

            for j in range(level):
                stick = Stick((delta_x[i], y))
                self.add(stick)
                delta_x[i] += stick.rect.width + delta_space[i]

            y += stick.rect.height + 5

    def removeSelected(self):
        for stick in self.sprites():
            if stick.isSelected():
                #stick.kill()
                self.remove(stick)


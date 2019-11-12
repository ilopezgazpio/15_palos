import pygame
from random import shuffle
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
                stick = Stick((delta_x[i], y), i)
                self.add(stick)
                delta_x[i] += stick.rect.width + delta_space[i]

            y += stick.rect.height + 5

    def removeSelected(self):

        sticks_selected = [stick for stick in self.sprites() if stick.isSelected()]
        number = len(sticks_selected)
        line = sticks_selected[0].line

        # stick.kill()
        [self.remove(stick) for stick in sticks_selected ]
        return (line,number)


    def removeMovement(self, tuple_xy):
        line, number = tuple_xy
        sticks_in_line = [stick for stick in self.sprites() if stick.line == line]

        shuffle(sticks_in_line)
        selected_sticks = sticks_in_line[:number]
        [selected.removeAI() for selected in selected_sticks]



from Scene import Scene
import pygame
import time
import utils

class VSFileNotFoundScene(Scene):

    def __init__(self, args = {}):
        '''Initialize'''
        Scene.__init__(self, args)

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(utils.BLACK)
        dimension = screen.get_size()
        (surface, rectangle) = utils.get_surfrect_text('Agent not trained!', 'arial', 42, utils.RED, dimension[0] / 2, dimension[1] / 2)
        screen.blit(surface, rectangle)
        self.showing = False






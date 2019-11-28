from Scene import Scene
import pygame
import time
import utils

class GameOverScene(Scene):

    def __init__(self, message, args = {}):
        '''Initialize'''
        Scene.__init__(self, args)

    def handle_events(self, events):
        self.next_scene = None
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                self.next_scene = 'GameScene'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                self.showing = False

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(utils.BLACK)
        dimension = screen.get_size()
        (surface, rectangle) = utils.get_surfrect_text('Play again ? (y/n)', 'arial', 55, utils.RED, dimension[0] / 2, dimension[1] / 2)
        screen.blit(surface, rectangle)
        #self.showing = False

import pygame
from Point import Point
from Stick import Stick
from Sticks import Sticks
from Scene import Scene
import os

class GameScene(Scene):

    def __init__(self, args = {}):
        '''Initialize'''
        Scene.__init__(self, args)

        ''' define local objects and sprites '''

        # Read agent Vs files
        if not os.path.exists(args.path):
            print("File {0} with V(s) values of agent does not exist. First run training script".format(args.path))
            self.showing = False
            self.next_scene = 'VSFileNotFoundScene'

        ''' define background '''
        self.background_image = pygame.image.load("resources/fieltro.jpg").convert()

        ''' Create objects of game'''
        # todo -> scene knows about args -> get args.resolution
        self.sticks = Sticks()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_sprite = Point(pygame.mouse.get_pos())
                stick_clicked = pygame.sprite.spritecollide(mouse_sprite, self.sticks, False)
                # Debug
                # mouse_sprite.printRect()
                # for stick in stick_clicked:
                #    stick.printRect()
                if stick_clicked:
                    stick_clicked[0].clicked()

            if event.type ==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                self.sticks.removeSelected()


    def update(self):
        '''Collitions'''
        pass

    def draw(self, screen):
        '''Fill screen background'''
        dimension = screen.get_size()
        self.background_image = pygame.transform.scale(self.background_image, dimension)
        screen.blit(self.background_image, [0,0])

        '''Draw sticks'''
        self.sticks.draw(screen)



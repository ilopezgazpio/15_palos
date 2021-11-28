import pygame
import sys
import time

# important to add scenes so they can be accessed through globals
from DummyScene import DummyScene
from GameScene import GameScene
from VSFileNotFoundScene import VSFileNotFoundScene
from GameOverScene import GameOverScene

class Director():

    def __init__(self, title = "The 15 sticks game", resolution = (620, 480)):
        '''Initialize'''
        self.current_scene = None
        self.resolution = resolution

        # dictionary containing sceneName => sceneObject
        self.game_scenes = {}

        check_errors = pygame.init()
        if check_errors[1] > 0:
            print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
            sys.exit(-1)

        # Game surface
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)

        # Set Clock
        self.clock = pygame.time.Clock()

        # Keyboard repetitions
        pygame.key.set_repeat(1000)

    def project_scene(self, scene_name, fps = 60):
        '''Project given scene'''
        self.current_scene = self.game_scenes[scene_name]
        self.showing = True

        while self.showing:

            self.clock.tick(fps)

            events = pygame.event.get()

            # Check events
            for event in events:
                if event.type == pygame.QUIT:
                    self.showing = False

            self.current_scene.handle_events(events)
            self.current_scene.update()
            self.current_scene.draw(self.screen)

            self.select_scene(self.current_scene.next_scene)

            if self.showing:
                self.showing = self.current_scene.showing

            pygame.display.flip()

        # closing game
        time.sleep(1)
        pygame.quit()
        sys.exit(0)

    def select_scene(self, next_scene_name, args = {}):

        if next_scene_name:
            if next_scene_name not in self.game_scenes:
                self.add_scene(next_scene_name, args)

            self.current_scene = self.game_scenes[next_scene_name]

    def add_scene(self, scene_name, args = {}):
        scene = globals()[scene_name]
        self.game_scenes[scene_name] = scene(args)


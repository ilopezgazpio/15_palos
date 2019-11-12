import sys

class Scene:

    def __init__(self, args = {}):
        '''Initialize'''
        self.args = args
        self.next_scene = None
        self.showing = True

    def handle_events(self, events):
        '''Handle events'''
        pass

    def update(self):
        '''Game logic'''
        pass

    def draw(self, screen):
        '''Draw scene'''
        pass

    def change_scene(self, scene):
        '''Change the scene to display in frame'''
        self.next_scene = scene

from Scene import Scene

class DummyScene(Scene):

    def __init__(self, args = {}):
        '''Initialize'''
        Scene.__init__(self, args)

        '''define local objects and sprites'''

    def handle_events(self, events):
        pass

    def update(self):
        '''Collitions'''
        pass

    def draw(self, screen):
        '''Fill screen color'''
        pass
        #screen.fill()


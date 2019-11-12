import pygame

class Point(pygame.sprite.Sprite):
    def __init__(self, tuplexy):
        self.x = tuplexy[0]
        self.y = tuplexy[1]
        super(pygame.sprite.Sprite, self).__init__()
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def printCoords(self):
        print("({},{})".format(self.x, self.y))

    def printRect(self):
        print("From ({},{}) , to ({},{})".format(self.x, self.y, self.x + self.rect.width, self.y + self.rect.width))
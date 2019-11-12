import pygame
import time

class Stick(pygame.sprite.Sprite):

    def __init__(self, location, line):
        pygame.sprite.Sprite.__init__(self)

        self.image_icon = 'resources/stick.png'
        self.x = location[0]
        self.y = location[1]
        # Line in which the stick is located line 0 -> 3 , line 1 -> 5 , line 2 -> 7
        self.line = line
        self.delete = False
        self.alpha = 0

        self.__load_image()

    def __load_image(self):
        # load image
        self.image = pygame.image.load(self.image_icon)

        # set rectangle
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.rect.width = self.image.get_rect().width
        self.rect.height = self.image.get_rect().height

    def clicked(self):
        if not self.isSelected():
            self.image_icon = 'resources/stick_selected.png'
            self.__load_image()
        else:
            self.image_icon = 'resources/stick.png'
            self.__load_image()

    def printCoord(self):
        print("({},{})".format(self.x, self.y))

    def printRect(self):
        print("From ({},{}) , to ({},{})".format(self.x, self.y, self.x + self.rect.width, self.y + self.rect.width))

    def isSelected(self):
        return self.image_icon == 'resources/stick_selected.png'



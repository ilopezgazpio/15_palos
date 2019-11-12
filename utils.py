import pygame

''' In-Game Colors '''
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)


'''Text render util'''
def get_surfrect_text(text, font, size, color, x, y):
    font = pygame.font.SysFont(font, size)
    surface = font.render(text, True, color)
    rectangle = surface.get_rect()
    rectangle.center = (x, y)
    return (surface, rectangle)



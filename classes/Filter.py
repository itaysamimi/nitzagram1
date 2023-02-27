from constants import *
import pygame
from helpers import screen


class Filter:
    def __init__(self, color, transparency):
        self.color = color
        self.transparency = transparency

    def filter_square(self):
        square = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        square.set_alpha(self.transparency)
        square.fill(self.color)
        screen.blit(square, (POST_X_POS, POST_Y_POS))

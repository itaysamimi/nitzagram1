import pygame
from helpers import screen
from constants import *


class Comment:
    """
    A class used to work with comments
    """
    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        font = pygame.font.SysFont('chalkduster.ttf', 15)
        txt = font.render(self.text, True, BLACK)
        screen.blit(txt, [FIRST_COMMENT_X_POS,
                          FIRST_COMMENT_Y_POS + COMMENT_LINE_HEIGHT * comment_num])

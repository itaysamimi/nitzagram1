from classes.Post import Post
from helpers import from_text_to_array, screen, center_text
import pygame
from constants import *
import pywhatkit


class TextPos(Post):
    def __init__(self, location, description, background_color, text, text_color):
        self.text_no_array = text
        Post.__init__(self, location, description)
        self.background = background_color
        self.text = from_text_to_array(text)
        self.text_color = text_color

    def display_content(self):
        square_post = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background, square_post)

        for line in range(len(self.text)):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text[line], True, self.text_color)

            to_center = center_text(len(self.text), text, line)
            screen.blit(text, to_center)

    def share(self, phnum):
        message = "Number of likes is {}.\n" \
                  "the location is {}.\n" \
                  "the description is {}"\
            .format(self.likes_counter, self.location, self.description)
        pywhatkit.sendwhatmsg_instantly(phnum, message)

    def to_list(self):
        return ['txt', self.location, self.description, self.likes_counter, self.text_no_array]
    
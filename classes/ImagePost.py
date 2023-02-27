from classes.Post import Post
import pygame
from constants import *
from helpers import screen
import pywhatkit


class ImagePost(Post):
    def __init__(self, image, location, description, filter=None):
        self.imgpath = image
        Post.__init__(self, location, description)
        self.image_src = pygame.image.load(image)
        self.image_src = pygame.transform.scale(self.image_src, (POST_WIDTH, POST_HEIGHT))
        self.filter = filter

    def display_content(self):
        screen.blit(self.image_src, (POST_X_POS, POST_Y_POS))
        if self.filter is not None:
            self.filter.filter_square()

    def share(self, phnum):
        message = "Number of likes is {}.\n" \
                  "the location is {}.\n" \
                  "the description is {}"\
            .format(self.likes_counter, self.location, self.description)
        pywhatkit.sendwhats_image(phnum, self.imgpath, message)

    def to_list(self):
        return ['img', self.location, self.description, self.likes_counter, self.imgpath]

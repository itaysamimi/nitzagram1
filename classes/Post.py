import pygame
from classes.Comment import Comment
from constants import *
from helpers import screen
import pywhatkit


class Post:
    """
    A class used to represent post on Nitzagram
    """
    user_name = 'itay'

    def __init__(self, location, description):
        # TODO: write me!
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_header(self):
        location_font = pygame.font.SysFont('chalkduster.ttf', 15)
        text = location_font.render(self.location, True, (134, 134, 134))
        screen.blit(text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        description_font = pygame.font.SysFont('chalkduster.ttf', 15)
        description_text = description_font.render(self.description, True, (50, 50, 50))
        screen.blit(description_text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        user_name_font = pygame.font.SysFont('chalkduster.ttf', 15)
        user_name_text = user_name_font.render(self.user_name, True, (50, 50, 50))
        screen.blit(user_name_text, [USER_NAME_X_POS, USER_NAME_Y_POS])

    def display_likes(self):
        likes_font = pygame.font.SysFont('chalkduster.ttf', 15)
        likes_text = likes_font.render('Liked by ' + str(self.likes_counter) + ' users', True, (0, 0, 0))
        screen.blit(likes_text, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def display_content(self):
        pass

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, comment_text):
        self.comments.append(Comment(comment_text))

    def view_more_comments(self):
        self.comments_display_index += 1
        self.comments_display_index = 0 \
            if self.comments_display_index == len(self.comments) \
            else self.comments_display_index

    def reset_comments_display_index(self):
        self.comments_display_index = 0

    def share(self, phnum):
        pass

    def to_list(self):
        pass






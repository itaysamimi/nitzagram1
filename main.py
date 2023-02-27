import pygame
from helpers import screen
from helpers import mouse_in_button, read_comment_from_user
from constants import *
from classes.ImagePost import ImagePost
from buttons import like_button, comment_button, click_post_button, view_more_comments_button, share_button
from classes.TextPost import TextPos
from classes.Filter import Filter

BAD_WORD = ['damn', 'fuck', 'cosemec']


def censor(com, list_com):
    if com in list_com:
        new_com = ''
        for i in range(len(com)):
            new_com += '*'

        return new_com
    return com


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    filter_ = Filter((54, 222, 144), 80)
    filter_.filter_square()
    noa_kirel_post = ImagePost(SRC_KIREL, 'Indinegev', 'boker tov', filter_)
    ronaldo_post = ImagePost(SRC_RONALDO, 'Midbern', 'layla tov')
    txt_post = TextPos('Tomorrowland', 'HAYDE MODE', BLUE, TXT, BLACK)

    post_list = [noa_kirel_post, ronaldo_post, txt_post]
    current_index = 0
    current_post = post_list[current_index]

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()

                if mouse_in_button(like_button, pos_mouse):
                    current_post.add_like()

                elif mouse_in_button(comment_button, pos_mouse):
                    the_comment = read_comment_from_user()
                    the_comment = censor(the_comment, BAD_WORD)
                    current_post.add_comment(the_comment)

                elif mouse_in_button(click_post_button, pos_mouse):
                    current_index += 1
                    current_index = 0 if current_index == len(post_list) else current_index
                    current_post = post_list[current_index]
                    current_post.reset_comments_display_index()

                elif mouse_in_button(view_more_comments_button, pos_mouse):
                    current_post.view_more_comments()

                elif mouse_in_button(share_button, pos_mouse):
                    number_phone = read_comment_from_user()
                    current_post.share(number_phone)

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()

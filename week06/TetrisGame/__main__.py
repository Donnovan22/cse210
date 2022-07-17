import pygame
import constants
from classes.director import Director


def main():

    pygame.init()

    # create the screen
    screen_size = (constants.MAX_X, constants.MAX_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(constants.CAPTION)

    # start the game
    director = Director(screen)
    director.start_game()

    pygame.quit()


if __name__ == "__main__":
    main()

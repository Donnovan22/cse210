import pygame
import constants
from classes.tetris import Tetris


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
       screen: For providing video output.
    """

    def __init__(self, screen):
        """Constructs a new Director.

        Args:
            screen:  the especific size of the window to be set.
        """
        self.done = False
        self.clock = pygame.time.Clock()
        self.game = Tetris(27, 13)
        self.counter = 0
        self.pressing_down = False
        self.screen = screen

    def start_game(self):
        """Starts the game. Runs the main game loop."""

        while not self.done:
            if self.game.figure is None:
                self.game.new_figure()
            self.counter += 1
            if self.counter > 100000:
                self.counter = 0

            if self.counter % (constants.FRAME_RATE // self.game.level // 2) == 0 or self.pressing_down:
                if self.game._state == "start":
                    self.game.go_down()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game.rotate_figure()
                    if event.key == pygame.K_DOWN:
                        self.pressing_down = True
                    if event.key == pygame.K_LEFT:
                        self.game.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        self.game.go_side(1)
                    if event.key == pygame.K_SPACE:
                        self.game.go_space()
                    if event.key == pygame.K_ESCAPE:
                        self.game.__init__(27, 13)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.pressing_down = False

            self.screen.fill(constants.BLACK)

            for i in range(self.game._height):
                for j in range(self.game._width):
                    pygame.draw.rect(self.screen, constants.WHITE, [self.game.x + self.game.zoom * j, self.game.y +
                                                                    self.game.zoom * i, self.game.zoom, self.game.zoom], 1)
                    if self.game.field[i][j] > 0:
                        pygame.draw.rect(self.screen, self.game.figure.colors[self.game.field[i][j]],
                                         [self.game.x + self.game.zoom * j + 1, self.game.y + self.game.zoom * i + 1, self.game.zoom - 2, self.game.zoom - 1])

            if self.game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in self.game.figure.image():
                            pygame.draw.rect(self.screen, self.game.figure.colors[self.game.figure._color], [
                                self.game.x + self.game.zoom * (j + self.game.figure._point.get_x()) + 1, self.game.y +
                                self.game.zoom * (i + self.game.figure._point.get_y()) + 1, self.game.zoom - 2, self.game.zoom - 2])

            font = pygame.font.SysFont(
                "Arial", constants.FONT_SIZE, True, False)
            font_1 = pygame.font.SysFont(
                "Arial", constants.FONT_SIZE_1, True, False)
            text = font.render("Score: " + str(self.game.score),
                               True, constants.WHITE)
            text_game_over = font_1.render("Game Over", True, constants.WHITE)
            text_game_over_1 = font_1.render(
                "Press ESC", True, constants.WHITE)
            text_game_over_2 = font_1.render(
                "To Play Again", True, constants.WHITE)

            self.screen.blit(text, [10, 0])
            if self.game._state == "gameover":
                self.screen.blit(text_game_over, [150, 300])
                self.screen.blit(text_game_over_1, [150, 400])
                self.screen.blit(text_game_over_2, [110, 500])

            pygame.display.flip()
            self.clock.tick(constants.FRAME_RATE)

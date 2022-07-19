from classes.point import Point
from classes.figure import Figure


class Tetris:
    """
    Building the game structure.

    The responsibility of Tetris is to create the field and figures with their respective actions(methods).

    Arguments:
        height (int): An integer value to set the height of the field(the grid)
        width (int): An integer value to set the width of the field(the grid)

    """

    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 30
    figure = None

    def __init__(self, height, width):
        self._height = height
        self._width = width
        self.field = []
        self.score = 0
        self._state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        """This method creates a new figure and position it at coordinates (5,0) which is the center of the field"""

        self.figure = Figure(Point(5, 0))

    def _intersects(self):
        """This method checks the current figure and recongnizes if when moving down touches the game field of another figure.
            When there is a intersection we need to freeze the figure on the field."""

        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure._point._y > self._height - 1 or \
                            j + self.figure._point._x > self._width - 1 or \
                            j + self.figure._point._x < 0 or \
                            self.field[i + self.figure._point._y][j + self.figure._point._x] > 0:
                        intersection = True
        return intersection

    def _break_lines(self):
        """This method checks if there is a full horizontal line that should be destroyed"""

        lines = 0
        for i in range(1, self._height):
            zeros = 0
            for j in range(self._width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for k in range(i, 1, -1):
                    for j in range(self._width):
                        self.field[k][j] = self.field[k - 1][j]
        self.score += lines ** 2

    def go_space(self):
        """This method makes the figure go directly to the bottom of the field by pressing the space key"""

        while not self._intersects():
            self.figure._point._y += 1
        self.figure._point._y -= 1
        self._freeze_figure()

    def go_down(self):
        """This method makes the figure go down until it reaches the bottom of the field or some fixed figure"""
        self.figure._point._y += 1
        if self._intersects():
            self.figure._point._y -= 1
            self._freeze_figure()

    def _freeze_figure(self):
        """This method freezes the current figures if there is an Intersection, 
        and after freezing creates a new Figure, and if it already intersects, the game is over"""

        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure._point._y][j +
                                                          self.figure._point._x] = self.figure._color
        self._break_lines()
        self.new_figure()
        if self._intersects():
            self._state = "gameover"

    def go_side(self, dx):
        """This method makes the figure move left or right"""
        old_x = self.figure._point._x
        self.figure._point._x += dx
        if self._intersects():
            self.figure._point._x = old_x

    def rotate_figure(self):
        """This method makes the figure rotate by pressing the up arrow key"""
        old_rotation = self.figure._rotation
        self.figure.rotate()
        if self._intersects():
            self.figure._rotation = old_rotation

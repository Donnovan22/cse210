import random
import constants


class Figure:
    """
    Differen types of figures.

    The responsibility of Figure is to store different figure types with the rotations.

    Arguments:
        point (Point()): the coordinates for the position of each figure in the grid
    """

    # list of colors
    colors = [
        constants.SKYBLUE,
        constants.BLUE,
        constants.ORANGE,
        constants.RED,
        constants.GREEN,
        constants.PURPLE,
        constants.BRONZE
    ]

    # list of figures
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # represents a line with the rotations
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # represents a z with the rotations
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # represents a z with the rotations
        # represents a L with the rotations
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        # represents a L with the rotations
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        # represents a pyramid with the rotations
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]]  # represents a square
    ]

    def __init__(self, point):
        self._point = point
        self._type = random.randint(0, len(self.figures) - 1)
        self._color = random.randint(1, len(self.colors) - 1)
        self._rotation = 0

    def image(self):
        return self.figures[self._type][self._rotation]

    def rotate(self):
        self._rotation = (self._rotation + 1) % len(self.figures[self._type])

from re import S
import constants
from classes.casting.actor import Actor
from classes.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self, x, y, main_color=constants.YELLOW, secondary_color=constants.GREEN):
        super().__init__()
        self._segments = []
        self._main_color = main_color
        self._secondary_color = secondary_color
        self._prepare_body(x, y, main_color, secondary_color)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        for i in range(number_of_segments):
            trail = self._segments[-1]
            velocity = trail.get_velocity()
            offset = velocity.reverse()
            position = trail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("*")
            segment.set_color(self._secondary_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self, x, y, main_color, secondary_color):
        x = int(x)
        y = int(y)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "O" if i == 0 else "*"
            color = main_color if i == 0 else secondary_color

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def set_main_color(self, color):
        self._main_color = color

    def set_secondary_color(self, color):
        self._secondary_color = color

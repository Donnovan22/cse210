from classes.casting.actor import Actor


class Score(Actor):
    """
    A record of points made. 

    The responsibility of Score is to add one point whether any player wins the game.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._points}")

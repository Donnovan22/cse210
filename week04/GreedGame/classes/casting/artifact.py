
from classes.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 

    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _score (int): the Artifact's score
    """

    def __init__(self):
        super().__init__()
        self._score = 0

    def get_score(self):
        """Gets the artifact's score.

        Returns:
            int: The message.
        """
        return self._score

    def set_score(self, score):
        """Updates the score to the given one.

        Args:
            score (int): The given score.
        """
        self._score = score

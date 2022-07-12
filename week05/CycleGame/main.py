from itertools import cycle
import constants

from classes.casting.actor import Actor
from classes.casting.cast import Cast
from classes.casting.food import Food
from classes.casting.score import Score
from classes.casting.cycle import Cycle
from classes.scripting.script import Script
from classes.scripting.control_actors_action import ControlActorsAction
from classes.scripting.move_actors_action import MoveActorsAction
from classes.scripting.handle_collisions_action import HandleCollisionsAction
from classes.scripting.draw_actors_action import DrawActorsAction
from classes.directing.director import Director
from classes.services.keyboard_service import KeyboardService
from classes.services.video_service import VideoService
from classes.shared.color import Color
from classes.shared.point import Point


def main():

    # create the cast
    cast = Cast()
    score = Score()
    score2 = Score()
    actor = Score()
    actor2 = Score()

    # create labels for palyer one and player two
    actor.set_text("Player One (Green) ( w, s, a, d ) : ")
    actor2.set_text("Player Two (Red) ( i, j, k, l ) : ")

    # setting the position of the labels
    actor2.set_position(Point(630, 0))
    score.set_position(Point(250, 0))
    score2.set_position(Point(850, 0))

    # Create the snakes
    cycle = Cycle(300, 300, constants.GREEN, constants.GREEN)
    cycle2 = Cycle(300, 300, constants.RED, constants.RED)

    cast.add_actor("cycles", cycle)
    cast.add_actor("cycles2", cycle2)
    cast.add_actor("scores", score)
    cast.add_actor("scores2", score2)
    cast.add_actor("player", actor)
    cast.add_actor("player2", actor2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("collision", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()

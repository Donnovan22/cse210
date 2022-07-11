import constants

from classes.casting.cast import Cast
from classes.casting.food import Food
from classes.casting.score import Score
from classes.casting.snake import Snake
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
    #cast.add_actor("foods", Food())
    snake = Snake(200, 300)
    score = Score()

    cast.add_actor("snakes", snake)
    cast.add_actor("scores", score)

    cast2 = Cast()
    score2 = Score()
    snake2 = Snake(600, 300)
    score2.set_position(Point(800, 0))
    cast2.add_actor("snakes2", snake2)
    cast2.add_actor("scores2", score2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    #script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, cast2, script)


if __name__ == "__main__":
    main()

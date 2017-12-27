import Tkinter
import gameStatus


class Handler:

    def __init__(self, game):
        self.__game = game

    # More get and set functions go below here
    # WHY USE GET AND SET FUNCTIONS:
    # Some fields should remain unaccessible by the user
    # therefore unaccessible outside of this class.
    # We call this kind of field private field.
    # In Python, we can write it as __pos_x
    # These fields can be accessed only through get and set functions,
    # such as get_pos_x() and set_pos_x(parameter)


class Paddle:
    # In the easy version of Pong game,
    # this class is equivalent to the Player class.

    def __init__(self, handler, position):
        self.__handler = handler
        # All the fields initiated by the constructor go below here

    def judge_collision(self):
        "stub"

    def add_score(self):
        "stub"

    def render(self):
        "stub"

    def update(self):
        "stub"

    def get_handler(self):
        "stub"

    # More get and set functions go below here
    # WHY USE GET AND SET FUNCTIONS:
    # Some fields should remain unaccessible by the user
    # therefore unaccessible outside of this class.
    # We call this kind of field private field.
    # In Python, we can write it as __pos_x
    # These fields can be accessed only through get and set functions,
    # such as get_pos_x() and set_pos_x(parameter)


class Ball:

    def __init__(self, handler):
        self.__handler = handler
        # All the fields initiated by the constructor go below here

    def judge_score(self):
        "stub"

    def hit(self):
        "stub"

    def render(self):
        "stub"

    def update(self):
        "stub"

    def get_canvas_width(self):
        "stub"

    def get_canvas_height(self):
        "stub"

    def get_handler(self):
        "stub"

    # More get and set functions go below here
    # WHY USE GET AND SET FUNCTIONS:
    # Some fields should remain unaccessible by the user
    # therefore unaccessible outside of this class.
    # We call this kind of field private field.
    # In Python, we can write it as __pos_x
    # These fields can be accessed only through get and set functions,
    # such as get_pos_x() and set_pos_x(parameter)


class Game:

    def __init__(self):
        self.__handler = handler
        # All the fields initiated by the constructor go below here

    def render(self):
        "stub"

    def update(self):
        "stub"

    def run(self):
        "stub"

    # More get and set functions go below here
    # WHY USE GET AND SET FUNCTIONS:
    # Some fields should remain unaccessible by the user
    # therefore unaccessible outside of this class.
    # We call this kind of field private field.
    # In Python, we can write it as __pos_x
    # These fields can be accessed only through get and set functions,
    # such as get_pos_x() and set_pos_x(parameter)

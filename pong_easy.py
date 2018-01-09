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

    def get_game(self):
        "stub"

    def get_paddle(self, index):
        "stub"

    def get_ball(self):
        "stub"

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

    def move_left(self):
        "stub"

    def move_right(self):
        "stub"

    def render(self, canvas):
        "stub"

    def update(self):
        "stub"

    # More get and set functions go below here
    # WHY USE GET AND SET FUNCTIONS:
    # Some fields should remain unaccessible by the user
    # therefore unaccessible outside of this class.
    # We call this kind of field private field.
    # In Python, we can write it as __pos_x
    # These fields can be accessed only through get and set functions,
    # such as get_pos_x() and set_pos_x(parameter)

    def get_canvas_width(self):
        "stub"

    def get_canvas_height(self):
        "stub"

    def get_padding(self):
        "stub"

    def get_pos_y(self):
        "stub"


class Ball:

    def __init__(self, handler):
        self.__handler = handler
        # All the fields initiated by the constructor go below here

    def judge_score(self):
        "stub"

    def hit(self):
        "stub"

    def render(self, canvas):
        "stub"

    def update(self):
        "stub"

    def get_canvas_width(self):
        "stub"

    def get_canvas_height(self):
        "stub"

    # More get and set functions go below here
    # WHY USE GET AND SET FUNCTIONS:
    # Some fields should remain unaccessible by the user
    # therefore unaccessible outside of this class.
    # We call this kind of field private field.
    # In Python, we can write it as __pos_x
    # These fields can be accessed only through get and set functions,
    # such as get_pos_x() and set_pos_x(parameter)

    def get_width(self):
        return self.__width

    def get_velocity_x(self):
        return self.__velocity_x

    def get_velocity_y(self):
        return self.__velocity_y


class Game:

    def __init__(self):
        self.__handler = handler
        # All the fields initiated by the constructor go below here

    def start_new_game(self):
        "stub"

    def key_pressed_handler(self, event):
        "stub"

    def key_released_handler(self, event):
        "stub"

    def key_action(self):
        "stub"

    def render_score(self):
        "stub"

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

    def set_game_status(self, game_status):
        "stub"

    def get_game_status(self):
        "stub"

    def get_canvas_width(self):
        "stub"

    def get_canvas_height(self):
        "stub"

if __name__ == "__main__":
    my_game = Game()
    my_game.run()
    my_game.frame.mainloop()

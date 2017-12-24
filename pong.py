import gameStatus
import brickEffects
import playerEffects


class Handler:

    def __init__(self, game):
        self.__game = game
        "stub"

    def get_game(self):
        return self.__game

    # Other get_ and set_ functions will go here


class Paddle:

    def __init__(self, handler):
        self.__handler = handler
        "stub"

    def judge_collision(self):
        "stub"

    def update(self):
        "stub"

    def render(self, canvas):
        "stub"

    def get_handler(self):
        return self.__handler

    # Other get_ and set_ functions will go here


class Player:

    def __init__(self, handler):
        self.__handler = handler
        "stub"

    def update(self):
        "stub"

    def render(self, canvas):
        "stub"

    def get_handler(self):
        return self.__handler

    # Other get_ and set_ functions will go here


class Ball:

    def __init__(self, handler):
        self.__handler = handler
        "stub"

    def judge_score(self):
        "stub"

    def update(self):
        "stub"

    def render(self, canvas):
        "stub"

    def get_handler(self):
        return self.__handler

    # Other get_ and set_ functions will go here


class Bricks:

    class Brick:

        def __init__(self, handler):
            self.__handler = handler
            "stub"

        def get_handler(self):
            return self.__handler

    # Other get_ and set_ functions will go here


    def __init__(self, handler):
        self.__handler = handler
        "stub"

    def generate_brick(self):
        "stub"

    def remove_brick(self):
        "stub"

    def update(self):
        "stub"

    def render(self, canvas):
        "stub"

    def get_handler(self):
        return self.__handler

    # Other get_ and set_ functions will go here


class Game:

    def __init__(self):
        "stub"

    def start_new_game(self):
        "stub"

    def update(self):
        "stub"

    def render(self, canvas):
        "stub"

    def run(self):
        "stub"

    # Other get_ and set_ functions will go here


if __name__ == '__main__':
    my_game = Game()
    my_game.run()
    my_game.frame.mainloop()

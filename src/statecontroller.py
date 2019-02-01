from enum import Enum


maxstate = 5
error = False


class State(Enum):
    start, player, ai, gameover, incorrect = range(1, maxstate + 1)


def is_error():
    return error


def error(error_code):
    # throw error light or otherwise
    error = True
    print('error: ' + error_code)


"""
def refreshstate():
    # direct between states
    # call on model after each move
"""
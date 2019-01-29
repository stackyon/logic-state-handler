from enum import Enum

state = State.start;
maxstate = 5
error = False

class State(Enum):
    start, player, ai, gameover, incorrect = range(1, maxstate)

def refreshstate():
    # direct between states
    # call on model after each move

def is_error():
    return error

def error(error_code):
    # throw error light or otherwise
    error = True
    print('error: ' + error_code)

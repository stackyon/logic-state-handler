state = State.start;
maxstate = 5

class State:
    start, player, ai, gameover, incorrect = range(1, maxstate)

def refreshstate():
    # direct between states
    # call on model after each move

def error(error_code):
    # throw error light or otherwise
    print('error: ' + error_code)
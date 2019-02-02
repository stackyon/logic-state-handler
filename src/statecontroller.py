class Controller:
    max_state = 5
    move_error = False
    current_state = 'start'


def is_error():
    return error


def error(error_code):
    # throw error light or otherwise
    Controller.move_error = True
    Controller.current_state = 'error'
    print('error: ' + error_code)


def reset_state():
    Controller.current_state = 'start'


class Controller:
    current_state = 'wait'


def error(error_code):
    # throw error light or otherwise
    Controller.current_state = 'error'
    print('error: ' + error_code)


def is_error():
    return Controller.current_state == 'error'


def wait():
    # New info hasn't arrived
    Controller.current_state = 'wait'


def is_wait():
    return Controller.current_state == 'wait'


def ready():
    Controller.current_state = 'ready'


def is_ready():
    return Controller.current_state == 'ready'


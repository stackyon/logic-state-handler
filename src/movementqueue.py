class Queu:
    e = []


def add_move(move):
    for movement in move.movements:
        add_movement(movement)


def add_movement(movement):
    Queu.e.append(movement)


def to_string():
    representation = ''
    for movement in Queu.e:
        if movement.movement_type == 'up':
            start_string = 'pick up at'
        if movement.movement_type == 'down':
            start_string = 'put down at'
        representation += start_string + ' (' + str(movement.x) + ', ' + str(movement.y) + ')\n'
    return representation


def clear_queue():
    Queu.e = []

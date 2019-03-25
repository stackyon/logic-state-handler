class Queu:
    e = []


def add_move(move):
    for movement in move.movements:
        Queu.e.append(movement)


def add_movement(movement):
    Queu.e.append(movement)


def to_string():
    for movement in Queu.e:
        if movement.movement_type == 'up':
            start_string = 'pick up at'
        if movement.movement_type == 'down':
            start_string = 'put down at'
        return start_string + ' (' + str(movement.square_x) + ', ' + str(movement.square_y) + ')'

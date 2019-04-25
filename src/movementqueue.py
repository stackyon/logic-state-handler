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
        representation += movement_to_string(movement)
    return representation


def movement_to_string(movement):
    if movement.movement_type == 'up':
        start_string = 'pick up at'
    if movement.movement_type == 'down':
        start_string = 'put down at'
    return start_string + ' (' + str(movement.x) + ', ' + str(movement.y) + ')\n'


def movement_to_string_output(movement):
    movement_code = 'x,y,z'
    if movement.movement_type == 'up':
        movement_code = movement_code.replace('z', '0')
    elif movement.movement_type == 'down':
        movement_code = movement_code.replace('z', '1')
    movement_code = movement_code.replace('x', str(movement.x))
    movement_code = movement_code.replace('y', str(movement.y))
    return movement_code


def pop_move():
    movement = Queu.e.pop(0)
    return movement_to_string_output(movement)


def clear_queue():
    Queu.e = []

movement_queue = []


def add_move(move):
    for movement in move.movements:
        movement_queue.append(movement)


def add_movement(movement):
    movement_queue.append(movement)


def print_queue():
    for movement in movement_queue:
        if movement.movement_type == 'up':
            start_string = 'pick up at'
        if movement.movement_type == 'down':
            start_string = 'put down at'
        print(start_string + ' (' + str(movement.square_x) + ', ' + str(movement.square_y) + ')')

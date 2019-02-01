import movement
import move


# get a player move from an input string
def build_move(move_code):
    from_square = move_code[0:2]
    to_square = move_code[2:4]
    new_movements = []
    # 3 digit code, use enum to compare type digit
    from_coords = coordinates(from_square)
    to_coords = coordinates(to_square)
    new_movements.append(movement.Movement('up', from_coords[0], from_coords[1]))
    new_movements.append(movement.Movement('down', to_coords[0], to_coords[1]))
    new_move = move.Move(new_movements)
    return new_move


def coordinates(p_square_code):
    x_y = []
    x_y.append(ord(p_square_code[:1]) - 96)
    x_y.append(int(p_square_code[1:]))
    return x_y
    # return a tuple x,y for square number


def get_uci(p_move):
    uci_from = square_code(p_move.movements[0].square_x, p_move.movements[0].square_y)
    uci_to = square_code(p_move.movements[1].square_x, p_move.movements[1].square_y)
    return uci_from + uci_to


def square_code(x, y):
    return chr(x + 96) + str(y)


"""
def print_move(p_move):
    # use enum to get type
    # generate phrase eg "pick up at square H8"
"""
